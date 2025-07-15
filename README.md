# Bank-Management-System

A secure, scalable and modern **Bank Management System** built using Flask, SQLAlchemy and WTForms. Designed to simulate basic banking operations like account creation, authentication, balance management and transactions.

---

## Features

- User registration & login
- Account dashboard
- Secure client account (bcrypt hashed password/PIN)
- Deposit & withdraw
- Fund transfer (Transaction System)
- Transaction history
- WTForms based Form Validation
- Responsive & modern UI
- Scalable & modular code structure

---

## Tech Stack

- **Backend**: Python (Flask)
- **Backend Mathematical Computations**: C++ (via subprocess)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3 (Bootstrap & custom CSS), Jinja2 templates, JavaScript, WTForms
- **Security**: bcrypt (for password/PIN hashing)
- **Email Automation**: SendGrid API

---

## Security Features

- Passwords & PINs are hashed with bcrypt (stronger than standard SHA-2)
- CSRF protection via WTForms
- Modular & extensible codebase for integrating 2FA and other security layers later on
- Unique ID generation and critical computations offloaded to C++ for performance

---

## Design Philosophy

Inspired by real world banking systems but optimised for developer learning and open-source contribution. The architecture was carefully planned from the start to support scalability, modularity and secure transactions.

---

## Setup Instructions

1. **Clone the repo**
   `git clone https://github.com/avik43218/Bank-Management-System.git`

2. **Navigate to the project folder**
   `cd Bank_Management_System`

3. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. **Navigate to the cpp source folder and create executables**
   `cd src/cpp`
   ```bash
   for file in *.cpp; do
       g++ "$file" -o "${file%.cpp}.exe"
   done
   ```

5. **Navigate back to root folder and Install dependencies**
   `pip install -r requirements.txt`

6. **Run the app**
   `python run.py`

7. **Visit** `http://localhost:5000`

---

## Security Notice

This project is for educational/experimental purposes only. For production-grade deployments:

- Use HTTPS
- Integrate a more robust authentication system (e.g. JWT, OAuth)
- Validate inputs more aggressively

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

**Thank you for checking out this project!**<br />
**Made with passion & love for the web - Avik43218**
