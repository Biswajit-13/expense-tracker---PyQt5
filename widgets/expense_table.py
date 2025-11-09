from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt

class ExpenseTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setColumnCount(5)
        headers = ["ID", "Date", "Category", "Amount", "Description"]
        self.setHorizontalHeaderLabels(headers)

        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setVisible(False)
        self.setAlternatingRowColors(True)
        self.setSelectionBehavior(self.SelectRows)
        self.setEditTriggers(self.NoEditTriggers)

    def create_item(self, text):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        return item
