# Shows the first 10 multiples of a number

n = input("Enter a number: ")

print("The first 10 multiples of " + n + " are:")

for i in range(1, 11):
    # Need to cast n to int for multiplication since input() returns a string
    print(str(i) + "x" + n + " =", i * int(n))