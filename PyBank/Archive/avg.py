""" # Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length


# Test your function with the following:
print(average([1, 5, 9, 20, 30]))
#print(average(range(11))) """

# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total/length


# Test your function with the following:
#print(average([1, 5, 9, 20, 30]))
print(average(range(15)))
