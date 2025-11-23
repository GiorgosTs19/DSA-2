# 4. Modify the fruit shopping list program so we can use it for a general shopping list, in the following way:
#
# 1. The program must ask you if you have all the necessary items in the shopping list
# 2. If no, it should let you add items until you're happy with it
# 3. If yes, it should show a message showing the items

shopping_list = []

first_item = input("Add an item in your list: ")
shopping_list.append(first_item)

have_all_ingredients = input("Do you have all the items in your list? (y/n): ")

# Input validation to ensure the input is either 'y' or 'n'
while have_all_ingredients != "y" and have_all_ingredients != "n":
    have_all_ingredients = input("Please enter 'y' or 'n': ")

# Keep asking for more items until the user confirms they have all ingredients
while have_all_ingredients != "y":
    new_item = input("Add another item: ")
    shopping_list.append(new_item)
    # Again Omitting input validation here for simplicity, could create a function, but it's not in the scope of this task.
    have_all_ingredients = input("Do you have all the items in your list? (y/n): ")
    
# Check if the shopping list is empty
if len(shopping_list) == 0 :
    print("Your shopping list is empty.")
else:
    # When the list is complete and has items in it, print the items with a message.
    for i in range(0, len(shopping_list)):
        print("You have " + shopping_list[i] + " in your shopping list")
    
# 5. Modify the shopping list program so it lets you delete items from the shopping list (you can use the "remove" function).
remove = input("Do you want to remove any items from the shopping list? (y/n): ")

# Input validation to ensure the input is either 'y' or 'n'
while remove != "y" and remove != "n":
    remove = input("Please enter 'y' or 'n': ")
    
while remove == "y":
    item_to_remove = input("Enter the item you want to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
        print(item_to_remove + " has been removed from your shopping list.")
    else:
        print(item_to_remove + " is not in your shopping list.")
    # Again Omitting input validation here for simplicity and to keep things within the task's scope
    remove = input("Do you want to remove any more items from the shopping list? (y/n): ")
    
# When the user is done removing items from the list, print the items with a message.
for i in range(0, len(shopping_list)):
    print("You have " + shopping_list[i] + " in your shopping list")

