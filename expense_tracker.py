expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "amount": amount})
    print(f"Added {name} - ${amount:.2f}")

def view_expenses():
    if not expenses:
        print("No expenses yet.")
        return
    total = 0
    print("\nYour Expenses:")
    for e in expenses:
        print(f"- {e['name']}: ${e['amount']:.2f}")
        total += e['amount']
    print(f"\nTotal = ${total:.2f}")

def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
