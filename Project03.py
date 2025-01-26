# Define a list to store expenses
expenses = []

# Function to display expenses
def show_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\n--- Expense List ---")
        for idx, expense in enumerate(expenses, start=1):
            print(f"{idx}. {expense['description']} - ${expense['amount']:.2f}")
        print("--------------------")

# Function to add a new expense
def add_expense():
    description = input("Enter a description for the expense: ")
    try:
        amount = float(input("Enter the amount of the expense: "))
        expenses.append({"description": description, "amount": amount})
        print(f"Expense '{description}' of ${amount:.2f} added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

# Function to calculate and display the total expenses
def show_total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

# Function to delete an expense
def delete_expense():
    try:
        show_expenses()  # Display all expenses first
        choice = int(input("Enter the number of the expense to delete: ")) - 1  # User chooses the index to delete
        if 0 <= choice < len(expenses):
            removed_expense = expenses.pop(choice)
            print(f"Expense '{removed_expense['description']}' deleted successfully.")
        else:
            print("Invalid choice. Expense not found.")
    except ValueError:
        print("Please enter a valid number.")
    except IndexError:
        print("Invalid expense number. Please select a valid number.")

# Display menu options
def show_menu():
    print("\n--- Expense Tracker Menu ---")
    print("Hey Anas! Welcome to My World")
    print("1. Add a New Expense")
    print("2. View All Expenses")
    print("3. Show Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

# Handle user input
def handle_choice(choice):
    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expenses()
    elif choice == '3':
        show_total_expenses()
    elif choice == '4':
        delete_expense()
    elif choice == '5':
        print("Exiting the Expense Tracker. Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True

# Main program loop
while True:
    show_menu()
    user_choice = input("Enter your choice: ")
    if not handle_choice(user_choice):
        break