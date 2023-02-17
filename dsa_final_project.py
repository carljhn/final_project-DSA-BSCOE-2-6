# Pick any python project available on the internet that used "Data Structures and Algorithms" concept.
# Set it up and make it work on your pc.
# Push the code in your github before you do any changes.
# Make some modifications to the project. Any idea you want to add.
# Make a demo highlighting used data structure and algorithm and your modifications
# Push your code changes in github.
# Final checking Feb 18. Recorded demo.

print("="*20, "My Grocery List", "="*20)

myList = []
ready = input("Press 'y' if you are ready and 'n' if not: ")
if ready == "y":

    Program = True
    while Program:
        print("="*57)
        print("\nWelcome to you Grocery List!")
        print("A: Add item to your list.")
        print("B. Delete an item to your list.")
        print("C. Update an item to your list.")
        print("D. Count the number of items in your list.")
        print("E. Exit the program.")

        user_input = input("\nWhat do you want to do? Please enter the corresponding letter of the options: ").lower()

        if user_input == "a":
            new_item = input("What item do you want to add?: ")
            myList.append(new_item)
            print("="*57)
            print("An item has been added")
            for items in myList:
                 print("-", items)
