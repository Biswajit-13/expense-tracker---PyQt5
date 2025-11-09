from database import Database

db = Database()

dummy_expenses = [
    ("2025-10-01", "Food", 450.50, "Dinner with friends"),
    ("2025-10-02", "Rent", 12000.00, "Monthly apartment rent"),
    ("2025-10-03", "Entertainment", 800.00, "Movie and snacks"),
    ("2025-10-04", "Travel", 2200.75, "Weekend trip"),
    ("2025-10-05", "Shopping", 1500.00, "New clothes"),
    ("2025-10-06", "Food", 250.00, "Lunch at cafe"),
    ("2025-10-07", "Rent", 12000.00, "Monthly apartment rent"),
    ("2025-10-08", "Travel", 980.00, "Cab rides and tickets"),
    ("2025-10-09", "Entertainment", 500.00, "Concert ticket"),
    ("2025-10-10", "Shopping", 2200.00, "Gadgets and accessories"),
]

for exp in dummy_expenses:
    db.add_expense(*exp)

print("✅ Dummy expenses inserted successfully!")
