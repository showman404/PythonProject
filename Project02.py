# Conversion functions
def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilograms_to_pounds(kilograms):
    return kilograms * 2.20462
# Display menu options
def show_menu():
    print("\n--- Unit Converter Menu ---")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Miles")
    print("3. Celsius to Fahrenheit")
    print("4. Kilograms to Pounds")
    print("5. Exit")

# Get user choice
def get_choice():
    choice = input("Enter your choice (1/2/3/4/5): ")
    return choice
# Perform conversion
def perform_conversion(choice):
    if choice == '1':
        meters = float(input("Enter the value in meters: "))
        print(f"{meters} meters = {meters_to_kilometers(meters):.2f} kilometers")
    elif choice == '2':
        kilometers = float(input("Enter the value in kilometers: "))
        print(f"{kilometers} kilometers = {kilometers_to_miles(kilometers):.2f} miles")
    elif choice == '3':
        celsius = float(input("Enter the temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == '4':
        kilograms = float(input("Enter the weight in kilograms: "))
        print(f"{kilograms} kilograms = {kilograms_to_pounds(kilograms):.2f} pounds")
    elif choice == '5':
        print("Exiting the Unit Converter. Goodbye!")
        return False
    else:
        print("Invalid choice. Please try again.")
    return True
# Main program loop
while True:
    show_menu()
    user_choice = get_choice()
    if not perform_conversion(user_choice):
        break