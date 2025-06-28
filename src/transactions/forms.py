from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Regexp
from wtforms import StringField, TelField, SelectField, SubmitField


class TransactionForm(FlaskForm):

    sender_id = StringField("Sender's Account ID", validators=[DataRequired(), 
                                                    Regexp(r'(?=^.{20}$)^(SAV|CUR|BUS)502[0-9]{14}$',
                                                    message="Enter a valid account ID!")])
    receiver_id = StringField("Receiver's Account ID", validators=[Regexp(r'(?=^.{20}$)^(SAV|CUR|BUS)502[0-9]{14}$',
                                                    message="Enter a valid account ID!")])
    amount = TelField("Transaction Amount", validators=[DataRequired(),
                                                    Regexp(r'^[1-9][0-9]*\.[0-9]+$',
                                                    message="Enter a valid amount!")])
    txn_type = SelectField("Transaction Type", validators=[DataRequired()], choices=[
        ('', ''), ('deposit', 'Deposit'), ('withdraw', 'Withdraw'), ('transfer', 'Transfer')
    ])
    security_pin = TelField("Transaction PIN", validators=[DataRequired(),
                                                    Regexp(r'^[1-9]{1}[0-9]{5}',
                                                    message="Enter a valid security PIN!")])
    submit = SubmitField("Make Payment")
