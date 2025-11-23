# Splits a list into even and odd elements

data = [9, 4, 5, 17, 12, 14, 1, 0, 3, 10, 9]

even = []
odd = []

for i in range(len(data)):
    print(i, data[i])
    if data[i] % 2 == 0:
        # Found an even element
        even.append(data[i])
    # Replaced the pop call. It now appends to a different array instead
    # to avoid changing the length of the list while iterating over it
    else:
        odd.append(data[i])

print("The even elements are: " + str(even))

print("The odd elements are: " + str(odd))