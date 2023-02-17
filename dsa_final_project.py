# Pick any python project available on the internet that used "Data Structures and Algorithms" concept.
# Set it up and make it work on your pc.
# Push the code in your github before you do any changes.
# Make some modifications to the project. Any idea you want to add.
# Make a demo highlighting used data structure and algorithm and your modifications
# Push your code changes in github.
# Final checking Feb 18. Recorded demo.

#import the required module
from prettytable import PrettyTable

print("="*20, "My Grocery List", "="*20)

# options
features = "\n\nWelcome to you Grocery List! \nA: Add item to your list. \nB. Delete an item to your list. \nC. Update an item to your list. \nD. Count the number of items in your list. \nE. Exit the program. \nF. Check your list"
print(features)

myList = []

x = PrettyTable()
# function for the table
def my_list():
    x.field_names = ["My Items"]
    for i in myList:
        x.add_row([i])

    print(x.get_string(title="MY GROCERY LIST"))
    x.clear_rows()

Program = True
while Program:
    user_input = input("\nWhat do you want to do? Please enter the corresponding letter of the options: ").lower()
    
    #option A
    if user_input == "a":
        new_item = input("\nWhat item do you want to add?: ").lower()
        print("="*57)
        print("An item has been added")
        myList.append(new_item)

    # option B
    elif user_input == "b":
        while True:
            itemName = input("Enter the item you want to remove: ").lower()
            try:
                if itemName in myList:
                    confirm = input(f"Are you sure you want to delete {itemName} from the list? (y/n): ").lower()
                    if confirm == "y":
                        myList.remove(itemName)
                        print("="*57)
                        print("\nList updated!")
                        my_list()
                        break
                else:
                    print("Item not found.")
            
            except Exception:
                print("Something went wrong.")

    # option C
    elif user_input == "c":
        while True:
            itemName = input("\nPlease enter the item you want to update: ").lower()
            try:
                if itemName in myList:
                    confirm = input(f"\nAre you sure you want to update {itemName} from the list? (y/n): ").lower()
                    if confirm == "y":
                        updateItem = input(f"\nPlease enter the item that you want to change {itemName} with: ").lower()
                        index = myList.index(itemName)
                        myList[index] = updateItem
                        print("="*57)
                        print("\nList updated!")
                        my_list()
                        break
            except Exception:
                print("Something went wrong.")

    # option D
    elif user_input == "d":
        itemName = input("Enter the item in the list that you want to count: ").lower()
        if itemName in myList:
            counter = myList.count(itemName)
            print("="*57)
            print("The number of item is:")
            print(counter)
        else:
            print("="*57)
            print("Item not found.")

    # option E
    elif user_input == "e":
            exit = input("\nAre you sure you want to exit the program?(y/n): ").lower()
            if exit == "y":
                program = False
                print("\nThank you for using this program!")
                break
    
    # option F
    elif user_input == "f":
        my_list()
    
    elif user_input == "" or user_input == " ":
        print("Please enter something")

    else:
        print("Invalid number, please try again")

    # saves the input in a txt file

    txtFile = open("grocery_list.txt", "w")
    theList = "\n".join(myList)
    txtFile.writelines(theList)