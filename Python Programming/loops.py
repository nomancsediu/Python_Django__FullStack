
#Loops Syntax in Python
#---------------------
#for variable in range(start, stop, step):
    #print(variable)


#Loops in Python
#---------------------
for i in range(1,11,2): #start, stop, step
    print(i)


#Reverse loop
#---------------------
for i in range(10,0,-1): #start, stop, step
    print(i)


#While loop
#---------------------
i = 1
while i<=10:
    print(i)
    i=i+3 #incrementing the value of i by 1


#Using time.sleep() to create a delay
#-------------------------------------

import time

for i in range(5,0,-1):
    print(i)
    time.sleep(1) #delay of 1 second
print("Time's up!")


#Project 4: Countdown Timer
#-------------------------------------

import time

#Taking user input for countdown time
start = int(input("Enter the number to start countdown from: "))

print("\n---- Countdown Timer ----")
print("Starting countdown...")

while start > 0:
    print(start)
    time.sleep(1) #delay of 1 second
    start=start-1 #decrementing the value of start by 1

print("Time's up!")

#End of the code



