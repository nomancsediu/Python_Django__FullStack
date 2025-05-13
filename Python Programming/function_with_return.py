# Temperature Converter (Project)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

# Display the menu
def show_menu():
    print("Temperature Converter Menu:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
        elif choice == '2':
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C = {celsius_to_kelvin(c):.2f}K")
        elif choice == '3':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
        elif choice == '4':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F = {fahrenheit_to_kelvin(f):.2f}K")
        elif choice == '5':
            k = float(input("Enter temperature in Kelvin: "))
            print(f"{k}K = {kelvin_to_celsius(k):.2f}°C")
        elif choice == '6':
            k = float(input("Enter temperature in Kelvin: "))
            print(f"{k}K = {kelvin_to_fahrenheit(k):.2f}°F")
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
        print()  # Add a blank line for spacing

# Run the program
if __name__ == "__main__":
    main()
