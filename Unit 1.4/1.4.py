# A. Hello World! in Python
print("Hello World!")

# B. Defining variables
my_integer = 3
my_float = 3.1
my_string = "This is a string"
my_fruit_list = ["Apples", "Oranges", "Bananas"]

# C. User input
input_name = input("Please enter your name: ")

# D. String output
print("Your name is: " + input_name)

# E. While loop
while len(my_fruit_list) < 5:
    new_fruit = input("You need to eat more fruit, enter another fruit: ")
    my_fruit_list.append(new_fruit)

# F. For loop
for i in range(0, len(my_fruit_list)):
    print("You have " + my_fruit_list[i] + " in your shopping list")

# G. If statement
have_all_ingredients = input("Do you have all the fruits in your list? (y/n): ")

if have_all_ingredients != "y":
    print("You should go to the grocery store")
