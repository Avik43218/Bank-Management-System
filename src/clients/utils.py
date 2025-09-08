def send_account_mail(account_id: str, full_name: str, email: str, account_type: str):

    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    first_name = full_name.split()[0]

    content = f"""
Hello {first_name.capitalize()},

Your new bank account has been created successfully with the following details:

    Account ID : {account_id}
    Account Holder's Name : {full_name.title()}
    Email Address : {email}
    Account Type : {account_type.capitalize()}

You can now login and manage your account from our secure portal.

Reminder: You password and PIN are never sent via email.

If you did not create this account, then please contact our support team immediately.

Thanks,
XYZ Bank Team
"""
    
    sender_email = os.getenv("EMAIL_USERNAME")
    message = Mail(
        from_email=sender_email,
        to_emails=email,
        subject="Welcome to XYZ Bank - Your account details",
        plain_text_content=content
        )
    
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    sg.send(message=message)


def send_registration_mail(client_id: str, full_name: str, contact: str, aadhar: str, email: str):

    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    first_name = full_name.split()[0]

    content = f"""
Hello {first_name.capitalize()},

Your User Account has been created successfully, with the credentials down below:

    Client ID : {client_id}
    Client's Name : {full_name}
    Aadhar : {aadhar}
    Contact : {contact}

Note: Passwords & PINs are never sent through email.

If you did not create this account, contact us immediately through our helpline number.
Contact Us : 1800-123-4567

Thank you for choosing us!
XYZ Bank Group
"""
    
    sender_email = os.getenv("EMAIL_USERNAME")
    message = Mail(
        from_email=sender_email,
        to_emails=email,
        subject="XYZ Bank - User Account Creation",
        plain_text_content=content
    )

    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    sg.send(message=message)


def send_account_mail_via_smtp(client_id: str, full_name: str, email: str, aadhar: str, contact: str):

    import os
    from src import mail
    from flask_mail import Message

    msg = Message('XYZ Bank - User Registration Notification', 
                  sender=os.getenv("EMAIL_USERNAME"), recipients=[email])
    
    first_name = full_name.split()[0]

    content = f"""
Hello {first_name.capitalize()},

Your User Account has been created successfully, with the credentials down below:

    Client ID : {client_id}
    Client's Name : {full_name}
    Aadhar : **** **** {aadhar[-4:]}
    Contact : ********{contact[-2:]}

Note: Passwords & PINs are never sent through email.

If you did not create this account, contact us immediately through our helpline number.
Contact Us : 1800-123-4567

Thank you for choosing us!
XYZ Bank Group
"""
    
    msg.body = content
    mail.send(msg)
