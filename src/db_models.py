from flask_login import UserMixin
from src import db, login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    try:
        return Client.query.get(int(user_id)) if user_id else None
    except (ValueError, TypeError):
        return None


class Client(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String(30), unique=True, nullable=False)
    full_name = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    aadhar = db.Column(db.Integer, unique=True, nullable=False)
    passwd = db.Column(db.String(64), nullable=False)
    accounts = db.relationship('Account', backref='owner', lazy=True)

    def __repr__(self):
        return f"Client('{self.full_name}', '{self.email}', '{self.aadhar}')"
    

class Account(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(20), unique=True, nullable=False)
    account_type = db.Column(db.String(10), nullable=False)
    voter_id = db.Column(db.String(10), unique=True, nullable=False)
    pan = db.Column(db.String(10), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    security_pin = db.Column(db.Integer, nullable=False)
    acc_owner_id = db.Column(db.String(30), db.ForeignKey('client.client_id'), nullable=False)

    def __repr__(self):
        return f"Account('{self.account_id}', '{self.balance}')"


class Transaction(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(20), db.ForeignKey('account.account_id'))
    receiver = db.Column(db.String(20), db.ForeignKey('account.account_id'))
    amount = db.Column(db.Float, nullable=False, default=0.0)
    txn_type = db.Column(db.String(20), nullable=False, default='')
    notes = db.Column(db.String(100), nullable=False, default='')
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
