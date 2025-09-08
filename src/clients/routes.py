from flask import Blueprint, redirect, url_for, flash, render_template, request
from flask_login import current_user, login_user, login_required, logout_user
from datetime import timedelta
import subprocess, os, certifi

from src.clients.forms import ClientRegistrationForm, ClientLoginForm, AccountCreationForm
from src.clients.utils import send_account_mail, send_account_mail_via_smtp
from src.db_models import Client, Account
from src import bcrypt, db, limiter


clients = Blueprint('clients', __name__)

@clients.route("/register_client", methods=["GET", "POST"])
@limiter.exempt
def register_client():

    if current_user.is_authenticated:
        return redirect(url_for("main.root_route"))
    
    form = ClientRegistrationForm()

    if form.validate_on_submit():
        hashed_passwd = bcrypt.generate_password_hash(form.current_password.data).decode('utf-8')
        
        # Generate Client ID
        id_generator_path = "src\\cpp\\client_id_generator.exe"
        uid = subprocess.run([id_generator_path, str(form.aadhar.data), str(form.contact.data)],
                             capture_output=True, text=True)
        
        if uid.returncode != 0:
            raise RuntimeError("Client registration process failed: " + uid.stderr)
        
        client = Client(client_id=uid.stdout.strip(),
                        full_name=form.full_name.data.lower(),
                        dob=form.dob.data,
                        address=form.address.data.lower(),
                        email=form.email.data.lower(),
                        contact=form.contact.data, 
                        aadhar=form.aadhar.data,
                        passwd=hashed_passwd
                        )

        db.session.add(client)
        db.session.commit()

        os.environ['SSL_CERT_FILE'] = certifi.where()

        send_account_mail_via_smtp(client_id=uid.stdout.strip(), full_name=form.full_name.data, 
                                   email=form.email.data, aadhar=str(form.aadhar.data), 
                                   contact=str(form.contact.data))

        flash("You have been registered successfully!", 'success')
        return redirect(url_for("clients.login"))
    
    return render_template("register_client.html", title="Registration", form=form)


@clients.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("main.root_route"))

    form = ClientLoginForm()

    if form.validate_on_submit():
        
        client = Client.query.first()

        if form.full_name.data.lower() == client.full_name and form.email.data.lower() == client.email\
             and form.aadhar.data == client.aadhar and bcrypt.check_password_hash(client.passwd, 
                                                                form.current_password.data):
            
            login_user(client, remember=form.remember_me.data, duration=timedelta(days=30))
            next_page = request.args.get('next')

            flash("You have been logged in successfully!", 'success')
            return redirect(next_page) if next_page else redirect(url_for("main.root_route"))

        else:
            flash("Invalid credentials! Please try again!", 'danger')
    return render_template("login.html", title="Login", form=form)


@clients.route("/create_account")
@login_required
def create_account():

    if not current_user.is_authenticated:
        return redirect(url_for("main.root_route"))
    
    form = AccountCreationForm()

    if form.validate_on_submit():

        hashed_pin = bcrypt.generate_password_hash(form.security_pin.data).decode("utf-8")

        # Generate Client ID
        path = "src\\cpp\\account_id_generator.exe"
        uid = subprocess.run([path, str(form.account_type.data), str(form.aadhar.data), 
                              str(current_user.client_id)], capture_output=True, text=True)
        
        if uid.returncode != 0:
            raise RuntimeError("Account creation process failed: ", uid.stderr)
        
        account = Account(
            account_id=uid.stdout.strip(),
            account_type=form.account_type.data,
            voter_id=form.voter_id.data,
            pan=form.pan.data,
            security_pin=hashed_pin
        )

        db.session.add(account)
        db.session.commit()

        os.environ['SSL_CERT_FILE'] = certifi.where()

        send_account_mail(account_id=str(uid.stdout.strip()), full_name=form.full_name.data,
                          email=form.email.data, account_type=form.account_type.data)
        
        flash("Account has been created successfully!", 'success')
        return redirect(url_for("main.root_route"))   # Later change this to clients.accounts

    return render_template("create_account.html", title="Account Creation")


@clients.app_errorhandler(429)
def ratelimit_handler(e):

    flash(F"Too many attempts, please try again later!", 'danger')
    return redirect(url_for('main.root_route'))


@clients.route("/logout")
def logout():

    logout_user()
    return redirect(url_for('main.root_route'))
