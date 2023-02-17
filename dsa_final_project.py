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
features = "\n\nWelcome to you Grocery List! \nA: Add item to your list. \nB. Delete an item to your list. \nC. Update an item to your list. \nD. Count the number of items in your list. \nE. Exit the program. \nCheck your list"
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

        if user_input == "a":
            new_item = input("What item do you want to add?: ")
            myList.append(new_item)
            print("="*57)
            print("An item has been added")
            for items in myList:
                 print("-", items)

        elif user_input == "b":
            itemName = input("Enter the item you want to remove: ")
            if itemName in myList:
                myList.remove(itemName)
                print("="*57)
                print("An item has been deleted")
                for items in myList:
                    print("-", items)
            else:
                print("="*57)
                print("Item not found.")

        elif user_input == "c":
            itemName = input("Enter your chosen item here: ")
            if itemName in myList:
                new_item = input("What item do you want to modify?: ")
                index = myList.index(itemName)
                myList[index] = new_item
                print("="*57)
                print("List updated!")
                for items in myList:
                    print("-", items)
            else:
                print("="*57)
                print("Item not found.")

        elif user_input == "d":
            itemName = input("Enter the item in the list that you want to count: ")
            if itemName in myList:
                counter = myList.count(itemName)
                print("="*57)
                print("The number of item is:")
                print(counter)
            else:
                print("="*57)
                print("Item not found.")

        elif user_input == "e":
                exit = input("\nAre you sure you want to exit the program?(y/n): ").lower()
                if exit == "y":
                    program = False
                    print("\nThank you for using this program!")
                    break

        else:
            print("Invalid number, please try again")