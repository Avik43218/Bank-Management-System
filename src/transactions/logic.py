def make_transaction(sender_acc_id: str, txn_type: str, amount: float, 
                     receiver_acc_id: str="", notes=""):
    
    from src.db_models import Account, Transaction
    from src import db

    sender = Account.query.filter_by(account_id=sender_acc_id).first()
    if not sender:
        return "Sender account not found!"
    
    if txn_type == "deposit":
        sender.balance += amount
        notes = f"{amount} has been credited to "
    
    elif txn_type == "withdraw":
        if sender.balance < amount:
            return "Insufficient account balance!"
        
        sender.balance -= amount

        notes = f"{amount} has been debited from "

    elif txn_type == "transfer":
        if receiver_acc_id[3:6] == "502":
            receiver = Account.query.filter_by(account_id=receiver_acc_id).first()
            if not receiver:
                return "Receiver account not found!"
            
            receiver.balance += amount
            sender.balance -= amount

            db.session.add(receiver)

        else:
            sender.balance -= amount

        receiver_log = Transaction(
            sender=sender_acc_id,
            receiver=receiver_acc_id,
            amount=amount,
            txn_type=txn_type,
            notes=notes
        )

        db.session.add(receiver_log)

    else:
        return "Invalid transaction type!"
    
    sender_log = Transaction(
        sender=sender_acc_id,
        receiver=receiver_acc_id,
        amount=amount,
        txn_type=txn_type,
        notes=notes
    )

    db.session.add_all([sender, sender_log])
    db.session.commit()

    return "Transaction successful!", notes
