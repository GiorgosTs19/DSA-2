# Adds the first n numbers

# Defined i
i = input("Please enter a number: ")

n = input("Please enter a second number: ")


# Cast both i and n to ints to allow for numerical operations
n = int(n)
i = int(i)

# Initialize total to 0
total = 0

while i < n:
    total = total + i
    i = i + 1

print("The total of the first " + str(n) + " numbers is " + str(total))