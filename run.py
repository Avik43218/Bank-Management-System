from src import create_app, db
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    inspector = inspect(db.engine)

    required_tables = ['client', 'account', 'transaction']
    existing_tables = inspector.get_table_names()

    missing = [table for table in required_tables if table not in existing_tables]

    if missing:
        print(f"Creating missing tables: {missing}")
        db.create_all()
    else:
        print("All required tables already exist.")


if __name__ == "__main__":
    app.run(debug=True)

