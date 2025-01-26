# Define functions for basic operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def square(a, b):
    return a ** b

# Display menu options
def show_menu():
    print("Hey ANAS! Welcome to the Simple Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. square (**)")
    print("6. Exit")

# Get user choice
def get_choice():
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    return choice
# Perform the calculation based on user choice
def calculate(choice):
    if choice in ['1', '2', '3', '4', '5']:
        # Get input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform operation
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", square(num1, num2))
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            return False
    else:
        print("Invalid choice! Please try again.")
    return True
# Main program loop
while True:
    show_menu()
    user_choice = get_choice()
    if not calculate(user_choice):
        break
def meters_to_kilometers(meters):
    return meters / 1000

meters = float(input("Enter the value in meters: "))
print(f"{meters} meters = {meters_to_kilometers(meters):.2f} kilometers")