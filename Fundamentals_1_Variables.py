# Defining text and integer variables:
my_name = 'Joe'
print(my_name)

my_fav_number = 321
print(my_fav_number)

# Updating variables:
# reassign a new value to the variable
my_name = 'Not Joe'
print(my_name)

# modify the existing variable
my_fav_number = my_fav_number + 100
print(my_fav_number)

# which you may also see written as
my_fav_number += 100
print(my_fav_number)

# Variables can also store other objects such as lists, dataframes, files. For Example:

# Creating a list of numbers:
numbers = [1,2,3,4,5]

# Creating a list of strings:
fruits = ["apple", "banana", "cherry"]

# Creating a mixed list:
mixed_list = [42, "Hello", 3.14, [1,2,3]]

# Printing the lists:
print(numbers)
print(fruits)
print(mixed_list)

# Accessing certain elements in the list (Note that 0 is the first position in the list):
first_fruit = fruits[0]
second_number = numbers[1]

print(first_fruit)
print(second_number)

# Exercise 1: 
# Objective: Finish a partially built calculator to understand variable assignments and basic arithmetic operations.

# Starting Code:
# Given values
number1 = 8
number2 = 4

# Sum - Complete the operation
sum_result = number1 + number2  # Replace None with the correct operation

# Product - Complete the operation
product_result = number1 * number2  # Replace None with the correct operation

# Print results (do not modify)
print(f"The sum of {number1} and {number2} is {sum_result}.")
print(f"The product of {number1} and {number2} is {product_result}.")

# Exercise 2: Favorite Foods List Manipulation
# Objective: Complete a script to manipulate a list of favorite foods and use string concatenation.

# Starting Code:
# Favorite foods list (do not modify)
favorite_foods = ["pizza", "sushi", "tacos", "pasta", "salad"]

# Print the entire list (Complete the code)
# TODO: Print the list here
print(*favorite_foods)
# note * will print the entire list with spaces in the middle as default

# Print the third item in the list (Complete the code)
# TODO: Print the third item here
third_item = favorite_foods[2]
print(third_item)

# Favorite food sentence (Complete the code)
favorite_sentence = f"My favorite food is {third_item}"  # Add the favorite food from the list
print(favorite_sentence)

# note the f infront of the string allows you to put in a variable
