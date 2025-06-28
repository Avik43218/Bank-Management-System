from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import current_user, login_required

from src.transactions.forms import TransactionForm
from src.transactions.logic import make_transaction


transaction = Blueprint('transaction', __name__)

@transaction.route("/make_transaction")
@login_required
def make_transaction():

    if not current_user.is_authenticated:
        return redirect(url_for("main.root_route"))
    
    form = TransactionForm()

    if form.validate_on_submit():

        receiver_id = form.receiver_id.data if form.receiver_id.data else ""
        
        result = make_transaction(
            sender_acc_id=form.sender_id.data,
            txn_type=form.txn_type.data,
            amount=float(form.amount.data),
            receiver_acc_id=receiver_id
        )

        flash(f"{result[1]}your account! An email has been sent to you!")
        return redirect(url_for("main.root_route"))
    
    return render_template("make_transaction.html", title="Transaction", form=form)
