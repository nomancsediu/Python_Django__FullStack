#Functions
def function_name():
    #Code block inside the function
    print("Hello, World!")

#Calling the function
function_name()

#Function with parameters
#-------------------------
def greet(name):
    print(f"Hello, {name}!")

greet("Noman")

def add(a,b):
    print(f"The sum is: {a+b}")

add(3,4)


def mul(a,b):
    return a*b

res = mul(5,4)
print("The result is:", res)

#Basic Math Quiz Game
#--------------------

import random

# Step 1: Define the math question function
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    else:
        ans = num1 * num2

    return f"{num1} {operator} {num2}", ans

# Step 2: Define the main game loop
def math_quiz():
    score = 0
    rounds = 5

    print("\n---Welcome to the Math Quiz Game!---")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(rounds):
        que, correct_ans = generate_question()
        print(f"\nQuestion {i+1}: {que}")
        user_ans = int(input("Your ans:"))

        if user_ans == correct_ans:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_ans}")

    # End of the game
    print("\n---Game Over!---")
    print(f"Your final score is: {score}/{rounds}")
    if score == rounds:
        print("Congratulations! You got all the questions correct.")
    elif score >= rounds // 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You can do better next time.")

# Start the quiz
math_quiz()
