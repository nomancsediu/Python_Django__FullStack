file = open("filename.txt","r")
content = file.read()   #Read
print(content)

with open ("filename.txt","w") as file:
    file.write("\nThis is a new note\n")  #Write

with open ("filename.txt","a") as file:
    file.write("\nThis is a new second note\n")  #Write


#Note Taking App (Project):
#--------------------------

#Step 1: Define file name

FILE_NAME = 'myNotes.txt'

def show_menu():
    print("\n---Note-Taking App Menu---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

def add_note():
    note = input("Enter your note: ")
    with open(FILE_NAME,"a") as file:
        file.write(note+"\n")
    print("Note added succesfully")

def view_notes():
    try:
       with open(FILE_NAME,"r") as file:
        content = file.read()
        if content:
            print("\n---Your Notes---")
            print(content)
        else:
            print("No notes found.")
    except FileNotFoundError:
        print("No notes Found.")

def del_note():
    confirm = input("Are you sure you want to delete all notes? (y/n): ")
    if confirm.lower()=='y':
        with open(FILE_NAME,'w') as file:
            pass
        print("All notes have been deleted.")
    else:
        print("Deletion cancel.")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_note()
    elif choice=='2':
        view_notes()
    elif choice=='3':
        del_note()
    elif choice =='4':
        print("Existing Note-Taking App. Goodbye!")
