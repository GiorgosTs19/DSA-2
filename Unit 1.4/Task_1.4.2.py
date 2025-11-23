# 2. Modify the program above so instead of defining the two integers in code, they are asked as an input from the user.
input_integer_one = input("Please enter the first integer: ")
input_integer_two = input("Please enter the second integer: ")

# Need to cast them to int before adding, since input() returns a string
input_sum = int(input_integer_one) + int(input_integer_two)

print("The input integer sum is: ",  input_sum)

