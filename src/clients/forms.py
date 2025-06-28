from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, TelField,
                     SelectField, DateField, BooleanField)
from wtforms.validators import Length, DataRequired, EqualTo, Regexp


class ClientRegistrationForm(FlaskForm):

    full_name = StringField('Full Name', validators=[DataRequired()])
    dob = DateField('Date of Birth', validators=[DataRequired()])
    address = StringField('Permanent Address', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Regexp(r'^[a-z0-9._+%-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                                                    message="Enter a valid email!")])
    contact = TelField('Phone Number', validators=[DataRequired(), Regexp(r'^\+?\d{10,12}$', 
                                                    message="Enter a valid phone number!")])
    aadhar = TelField('Aadhar Number', validators=[DataRequired(), Regexp(r'^\d{12}$',
                                                    message="Enter a valid aadhar number!")])
    current_password = PasswordField('Registration Password', validators=[DataRequired(),
                                                                    Length(min=8)])
    confirm_passwd = PasswordField('Confirm Password', validators=[DataRequired(),
                                                        Length(min=8), EqualTo('current_password')])
    data_verified = BooleanField('I hereby declare that the information provided is correct to my knowledge.', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AccountCreationForm(FlaskForm):

    full_name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Regexp(r'^[a-z0-9._+%-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                                                    message="Enter a valid email!")])
    aadhar = TelField('Aadhar Number', validators=[DataRequired(), Regexp(r'^\d{12}$',
                                                    message="Enter a valid aadhar number!")])
    account_type = SelectField('Account Type', validators=[DataRequired()], choices=[
        ('', ''), ('savings', 'Savings'), ('current', 'Current'), ('business', 'Business')
    ])
    voter_id = TelField('Voter ID Number', validators=[DataRequired(), Regexp(r'^[A-Z]{3}[0-9]{7}$',
                                                    message="Enter a valid voter ID number!")])
    pan = TelField('PAN Number', validators=[DataRequired(), Regexp(r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$',
                                                    message="Enter a valid PAN number!")])
    security_pin = TelField('Security PIN', validators=[DataRequired(), Regexp(r'^[0-9]{6}$',
                                                    message="Enter a valid PIN")])
    submit = SubmitField('Create Account')


class ClientLoginForm(FlaskForm):

    full_name = StringField("Account Holder's Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Regexp(r'^[a-z0-9._+%-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                                                    message="Enter a valid email address!")])
    aadhar = TelField('Aadhar Number', validators=[DataRequired(), Regexp(r'^\d{12}$',
                                                    message="Enter a valid aadhar number!")])
    current_password = PasswordField("Registration Password", validators=[DataRequired(), Length(min=8)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")
