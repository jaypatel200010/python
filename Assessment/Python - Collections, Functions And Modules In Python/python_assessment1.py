#Assessment: Core Python Assessment Test
#Jaylumar Patel
#Write a program to demonstrate the Python E-Note Book Console based application. 

import datetime

def generate_note():
    """Function to generate a note."""

    #inputs Generator name, title and content
    generator_name = input("Enter note generator name: ") 
    if not generator_name.isalpha():  # Check if input contains only letters
        print("Error: Invalid Input.")
        return  # Exit function if invalid input
    note_title = input("Enter note title: ")
    note_content = input("Enter note content: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] #for date and time

    #Added the data of input field to file through append method of file handling
    file = open("C:\\Users\\ASUS\\Desktop\\Tops\\python\\Assessment\\Python - Collections, Functions And Modules In Python\\jay.txt","a")
    
    file.write(f"-------------------------------------------------------\n{timestamp}\nE-Note Title: {note_title}\nE-Note Description: {note_content}\n                  Note Generator: {generator_name}\n\n")
    file.close()
    print("Note generated successfully.\n")
def view_note():
    """Function to view an existing note."""
    try:
        
        #Read the file through read method of file handling
        file = open("C:\\Users\\ASUS\\Desktop\\Tops\\python\\Assessment\\Python - Collections, Functions And Modules In Python\\jay.txt","r")
        print(file.readlines())
        file.close()
    except FileNotFoundError:
        print("Note does not exist.\n")

def main_menu():
    """Function displaying the main menu and handling user interaction."""
    while True:
        #menu
        print("Welcome to Python E - Note")
        print("Press 1 for generate Note")
        print("Press 2 for view Note")
        print("Press 3 for exit\n")

        choice = input("Enter your choice: ") #Taking choice from user

        if choice == '1':
            generate_note()
        elif choice == '2':
            view_note()
        elif choice == '3':
            break
        else:
            print("\nInvalid choice. Please try again.\n")

# Main execution point of the program.
if __name__ == "__main__":
    main_menu()
