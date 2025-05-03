#Variables in Python
#---------------------

#Storing a name in a variable 
nameOfPerson = "Abdullah Al Noman" #use camel case for variable names
#Storing an age in a variable
age = 20


#Datatypes in Python
#---------------------

#String
name = "Abdullah Al Noman"
#Float
height = 5.8 
#Boolean
isStudent = True

print(name)
print(height)
print(isStudent)
print(type(name))
print(type(height))
print(type(isStudent))

#Type Conversion
#---------------------

age = "22"
age = int(age)
print(age + 2)

#String Formatting
#---------------------

name = "Abdullah Al Noman"
print("My name is " + name)

print(f"My name is {name}") #f-string formatting


#Project 1: Personalized Greeting Message
#-----------------------------------------

name = input("What is your name?")
age = int(input("What is your age? "))
color = input("What is your favorite color? ")

print("\n---- Personalized Greeting Message ----")
print(f"Hello, {name}!👋 ")
print(f"You are {age} years old.")
print(f"Your favourite color is {color}.✨")
print(f"You are now ready to start your Python Adventure! 🚀")
