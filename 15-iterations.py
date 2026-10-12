"""EXAMPLES
1. Sequence of numbers from 1 to 10
2. A sequence of even numbers between 0 and 20 (inclusive)
3. A sequence of numbers from 1 to 10 with a step of 3
4. Print individual letters of a string "PYTHON"
5. Given the list numbers = [2, 7,10, 16, 23, 54] print a list of square of each
number in the list
6. Given the float_list = [2.5, 16.42, 10.77, 8.3, 34.21] print how many numbers are
less than 10."""

# Example 1: Sequence of numbers from 1 to 10
for i in range(1, 11):
    print(i, end=" ")
#example 2: A sequence of even numbers between 0 and 20 (inclusive)
for i in range(0, 21, 2):
    print(i, end=" ")
#example 3: A sequence of numbers from 1 to 10 with a step of 3
for i in range(1, 11, 3):
    print(i, end=" ")
#example 4: Print individual letters of a string "PYTHON"
string = "PYTHON"
for letter in string:
    print(letter, end=" ")
#example 5: Given the list numbers = [2, 7,10, 16, 23, 54] print a list of square of each number in the list
numbers = [2, 7, 10, 16, 23, 54]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)