"""

1. Write a Python function that accepts a string and calculate the number of upper-case letters
and lower-case letters
Sample string: PythOn
Number of Uppercase letters: 2
Number of Lowercase letters: 4
2. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
3. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output: 20

"""
# Function to calculate the number of upper-case and lower-case letters in a string
def count_case_letters(input_string):
    upper_case_count = 0
    lower_case_count = 0
    for char in input_string:
        if char.isupper():
            upper_case_count+= 1
        elif char.islower():
            lower_case_count += 1
    print(f"Number of Uppercase letters: {upper_case_count}")
    print(f"Number of Lowercase letters: {lower_case_count}")

count_case_letters("PythOn")

# Function to return the sum of multiples of 3 and 5 between 0 and limit
def sum_of_multiples(limit):
    total_sum = 0
    for i in range(0, limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

print(sum_of_multiples(20))

# Function to sum all the numbers in a list