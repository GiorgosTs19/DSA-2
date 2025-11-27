def request_sorted_array_input():
    input_array=[]
    array = input("Please enter a sorted array of integers, separated by spaces: ")
    string_numbers = array.split(" ")
    for stringNumber in string_numbers:
        input_array.append(int(stringNumber))
    return input_array


    