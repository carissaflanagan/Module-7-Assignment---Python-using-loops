# Check if numbers are even or odd
# Carissa Flanagan
# 7-23-2025

# Create a list of 15 numbers from 1 to 15
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

# Iterate through the list with a for loop
for number in numbers:
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
