#shopping_list = ["Milk", "Eggs", "Bread"]
#print(shopping_list)

#Accessing item from list
#------------------------
#print(shopping_list[2])

#shopping_list.append("Butter")
#print(shopping_list)

#shopping_list.remove("Bread")
#print(shopping_list)

#shopping_list.pop()
#shopping_list.pop(0)
#print(shopping_list)

#shopping_list = ["Milk", "Eggs", "Bread"]

#for item in shopping_list:
#    print(item)

#for index, item in enumerate (shopping_list):
#    print(f"{index+1}. {item}")


#List Methods More
#-----------------
#shopping_list = ["Milk", "Eggs", "Bread"]
#shopping_list.insert(1,"Juice")
#print(shopping_list)

#shopping_list.sort()
#print(shopping_list)

#shopping_list.reverse()
#print(shopping_list)

#shopping_list.clear()
#print(shopping_list)


#Project: Shopping List App
#--------------------------

shopping_list = []

def show_menu():
    print("\n--- Shopping List Menu ---")
    print("1. View the shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Clear list")
    print("5. Exit")

while(True):
    show_menu()
    choice = input("Enter your choice: ")

    if choice =='1':
        print("\n---Shopping List---")
        if not shopping_list:
         print("Your Shopping list is empty.")
        else:
          for index, item in enumerate(shopping_list):
            print(f"{index+1}.{item}")

    elif choice =='2':
       item = input("Enter the item to add: ")
       shopping_list.append(item)
       print(f"{item} has been added to the shopping list")
    
    elif choice == '3':
       item = input("Enter the item to remove: ")
       if item in shopping_list:
          shopping_list.remove(item)
          print(f"{item} has been removed from the shopping list.")
       else:
          print(f"{item} is not in the shopping list.")

    elif choice == '4':
       shopping_list.clear()
       print("The shopping list has been cleared.")
    
    elif choice =='5':
       print("Goodbye!Happy Shopping!")
       break
    else:
       print("Invalid choice. Please try again.")
       




   








