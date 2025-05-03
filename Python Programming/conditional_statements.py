number = 10

# Conditional Statements
#---------------------------

if number > 10:
    print("Number is greater than 10")
elif number == 10:
    print("Number is equal to 10")
else:
    print("Number is less than 10")


# Nested Conditional Statements
#---------------------------
if number > 0:
    print("Number is positive")
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
else:
    print("Number is negative")
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


#Logical Operators

a=7
b=12

if a > 5 and b < 15:
    print("Both conditions are true")
else:
    print("At least one condition is false")

if a > 5 or b < 10:
    print("At least one condition is true")
else:
    print("Both conditions are false")




#End of the code