import sqlite3

class Database:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_expense(self, date, category, amount, description):
        query = "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)"
        self.conn.execute(query, (date, category, amount, description))
        self.conn.commit()

    def fetch_expenses(self):
        query = "SELECT id, date, category, amount, description FROM expenses ORDER BY id DESC"
        return self.conn.execute(query).fetchall()
    
    def fetch_expense_by_id(self, expense_id):
        query = "SELECT id, date, category, amount, description FROM expenses WHERE id = ?"
        return self.conn.execute(query, (expense_id,)).fetchone()


    def delete_expense(self, expense_id):
        query = "DELETE FROM expenses WHERE id = ?"
        self.conn.execute(query, (expense_id,))
        self.conn.commit()
