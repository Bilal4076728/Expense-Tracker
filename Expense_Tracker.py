"""
Command-Line Expense Tracker
-----------------------------
A simple CLI application to add, view, delete, and analyze personal
expenses. Data is persisted locally using a JSON file.
"""

import json


class Expense:
    """Represents a single expense entry."""

    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        """Convert the Expense object into a dictionary (for JSON storage)."""
        return {
            "Amount": self.amount,
            "Category": self.category,
            "Description": self.description,
            "Date": self.date
        }

    def __str__(self):
        return f"Category: {self.category:<12} Rs. {self.amount:<8} {self.description:<20} Date: {self.date}"


class ExpenseTracker:
    """Manages a collection of Expense objects and handles persistence."""

    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description, date):
        """Create a new Expense and add it to the tracker."""
        new_expense = Expense(amount, category, description, date)
        self.expenses.append(new_expense)
        print("Expense added successfully.")

    def view_expenses(self):
        """Display all recorded expenses with their index."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        for index, expense in enumerate(self.expenses):
            print(f"[{index}] {expense}")

    def delete_expense(self, index):
        """Delete an expense by its index in the list."""
        if not self.expenses:
            print("No expenses to delete.")
            return

        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense deleted successfully.")
        else:
            print("Invalid index.")

    def total_by_category(self):
        """Print the total amount spent, grouped by category."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        totals = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount

        print("\n--- Total Spending by Category ---")
        for category, amount in totals.items():
            print(f"{category}: Rs. {amount}")

    def save_to_file(self, filename="data.json"):
        """Save all expenses to a JSON file."""
        data = [expense.to_dict() for expense in self.expenses]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    def load_from_file(self, filename="data.json"):
        """Load expenses from a JSON file, if it exists."""
        try:
            with open(filename, "r") as f:
                data = json.load(f)

            for item in data:
                expense = Expense(item["Amount"], item["Category"], item["Description"], item["Date"])
                self.expenses.append(expense)
        except FileNotFoundError:
            print("No saved data found. Starting fresh.")
        except json.JSONDecodeError:
            print("Save file is corrupted. Starting fresh.")


def get_valid_amount():
    """Prompt the user until a valid numeric amount is entered."""
    while True:
        try:
            return float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_valid_index(prompt):
    """Prompt the user until a valid integer index is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    tracker = ExpenseTracker()
    tracker.load_from_file()

    menu = """
1. Add Expense
2. View Expenses
3. Delete Expense
4. Total by Category
5. Save & Exit
"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            amount = get_valid_amount()
            category = input("Enter category: ")
            description = input("Enter description: ")
            date = input("Enter date (DD-MM-YYYY): ")
            tracker.add_expense(amount, category, description, date)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            index = get_valid_index("Enter the index of the expense to delete: ")
            tracker.delete_expense(index)

        elif choice == "4":
            tracker.total_by_category()

        elif choice == "5":
            tracker.save_to_file()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
