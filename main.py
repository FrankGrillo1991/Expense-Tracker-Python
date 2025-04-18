import csv
import os

FILENAME = "expenses.csv"

def initialize_csv():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Decription"])

def add_expense(date, category, amount, description):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
        print("Expense added!")

def view_expenses():
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    initialize_csv()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            description = input("Enter description")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Try again")

if __name__ == "__main__":
    main()
