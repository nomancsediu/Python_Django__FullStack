#Taking user input
#---------------------

name = input("Enter your name:")
print(f"Hello, {name}!")

#Type conversion
#---------------------

num1 = input("Enter a number:")
num1 = int(num1) #converting string to integer
print(f"Number doubled is: {num1*2}")

#Basic Arithmetic operations
#---------------------------

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
print(f"Remainder: {num1 % num2}")
print(f"Power: {num1 ** num2}")
print(f"Floor Division: {num1 // num2}")


#Simple Calculator
#---------------------------

#Taking user input for two numbers and an operator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

#Dispay the results
print("\n---- Simple Calculator ----")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")

#End of the code






