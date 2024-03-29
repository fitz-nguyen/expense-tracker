from expense import Expense
from datetime import datetime
import calendar

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    butget = 2000

    # Get user input for expense.
    # expense = get_user_expense()

    # Write their expense to a file.
    # save_expense_to_file(expense, expense_file_path)

    # Read file an summarize expenses.
    summarize_expenses(expense_file_path, butget)

    pass

def get_user_expense():
    print("Getting user expense...")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You've entered Name: {expense_name}, Amount: {expense_amount}")

    expense_category = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]
    while True:
        print("Select a category:")
        for i, cat in enumerate(expense_category):
            print(f"{i+1}. {cat}")
        try:
            value_range = f"[1 - {len(expense_category)}]"
            cat_index = int(input(f"Enter category number {value_range}: ")) - 1
            if cat_index < 0 or cat_index >= len(expense_category):
                raise ValueError
            else:
                selected_category = expense_category[cat_index]
                new_expense =  Expense(name=expense_name, 
                                     category= selected_category, 
                                     amount= expense_amount)
                return new_expense

        except ValueError:
            print("Invalid category number. Please try again.")


def save_expense_to_file(expense, expense_file_path="expenses.txt"):
    print(f"Saving User Expense: {expense} to file {expense_file_path}...")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

def summarize_expenses(expense_file_path, budget):
    print("Summarizing user expenses...")
    expenses = []
    with open(expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name=expense_name, 
                                   category=expense_category, 
                                   amount=float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expense By Category: ")
    for key, amount in amount_by_category.items():
        print(f"{key}: ${amount:.2f}")

    total_spent = sum(amount_by_category.values())
    print((f"Total Spent: ${total_spent:.2f}"))

    remaining_budget = budget - total_spent
    print((f"Budget Remaining: ${remaining_budget:.2f}"))

    now = datetime.now()
    _, num_days_in_month = calendar.monthrange(now.year, now.month)
    remaining_days = num_days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"Budget Per Day: ${daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == '__main__':
    main()