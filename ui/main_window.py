from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QLineEdit, QComboBox,
    QDateEdit, QVBoxLayout, QHBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from widgets.expense_table import ExpenseTable
from ui.style import APP_STYLE
from data.database import Database
from ui.expense_detail import ExpenseDetailWindow

class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("💰 Expense Tracker v1.01")
        self.resize(900, 700)
        self.setStyleSheet(APP_STYLE)

        # Initialize DB
        self.db = Database()

        self.setup_ui()
        self.load_expenses()
        self.table.cellDoubleClicked.connect(self.open_expense_detail)

    def setup_ui(self):
        # --- Widgets ---
        self.date_box = QDateEdit()
        self.date_box.setCalendarPopup(True)
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_button = QPushButton("＋ Add Expense")
        self.delete_button = QPushButton("🗑 Delete Expense")

        self.table = ExpenseTable()

        categories = ["Entertainment", "Rent", "Food", "Travel", "Shopping"]
        self.dropdown.addItems(categories)

        # --- Layouts ---
        self.master_layout = QVBoxLayout()
        self.master_layout.setContentsMargins(20, 20, 20, 20)
        self.master_layout.setSpacing(15)

        title = QLabel("💸 Expense Tracker")
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #0078d7; margin-bottom: 10px;")

        # Rows
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()

        for row in (row1, row2, row3):
            row.setSpacing(10)

        row1.addWidget(QLabel("Date:"))
        row1.addWidget(self.date_box)
        row1.addWidget(QLabel("Category:"))
        row1.addWidget(self.dropdown)

        row2.addWidget(QLabel("Amount:"))
        row2.addWidget(self.amount)
        row2.addWidget(QLabel("Description:"))
        row2.addWidget(self.description)

        row3.addStretch()
        row3.addWidget(self.add_button)
        row3.addWidget(self.delete_button)
        row3.addStretch()

        # Add layouts
        self.master_layout.addWidget(title)
        self.master_layout.addLayout(row1)
        self.master_layout.addLayout(row2)
        self.master_layout.addLayout(row3)
        self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)

        # --- Connect signals
        self.add_button.clicked.connect(self.add_expense)
        self.delete_button.clicked.connect(self.delete_expense)
       

    def load_expenses(self):
        """Fetch data from DB and populate table."""
        self.table.setRowCount(0)
        data = self.db.fetch_expenses()

        for row_num, row_data in enumerate(data):
            self.table.insertRow(row_num)
            for col_num, value in enumerate(row_data):
                self.table.setItem(row_num, col_num, self.table.create_item(str(value)))

    def open_expense_detail(self, row, column):
        expense_id_item = self.table.item(row, 0)  # First column = id
        if not expense_id_item:
           return

        expense_id = int(expense_id_item.text())
        expense = self.db.fetch_expense_by_id(expense_id)

        if expense:
            self.detail_window = ExpenseDetailWindow(expense)
            self.detail_window.show()


    def add_expense(self):
        """Add expense to DB and refresh table."""
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount_text = self.amount.text().strip()
        desc = self.description.text().strip()

        if not amount_text:
            QMessageBox.warning(self, "Validation Error", "Amount cannot be empty.")
            return

        try:
            amount = float(amount_text)
        except ValueError:
            QMessageBox.warning(self, "Validation Error", "Amount must be a number.")
            return

        self.db.add_expense(date, category, amount, desc)
        self.load_expenses()

        self.amount.clear()
        self.description.clear()

    def delete_expense(self):
        """Delete selected expense."""
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "No Selection", "Please select a row to delete.")
            return

        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(
            self,
            "Delete Confirmation",
            f"Are you sure you want to delete expense ID {expense_id}?",
            QMessageBox.Yes | QMessageBox.No,
        )

        if confirm == QMessageBox.Yes:
            self.db.delete_expense(expense_id)
            self.load_expenses()
