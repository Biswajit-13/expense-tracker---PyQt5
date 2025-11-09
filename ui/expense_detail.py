from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class ExpenseDetailWindow(QWidget):
    def __init__(self, expense, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Expense #{expense[0]} Details")
        self.resize(400, 300)

        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"🆔 ID: {expense[0]}"))
        layout.addWidget(QLabel(f"📅 Date: {expense[1]}"))
        layout.addWidget(QLabel(f"📂 Category: {expense[2]}"))
        layout.addWidget(QLabel(f"💰 Amount: ₹{expense[3]:.2f}"))
        layout.addWidget(QLabel(f"📝 Description: {expense[4]}"))

        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        self.setLayout(layout)
