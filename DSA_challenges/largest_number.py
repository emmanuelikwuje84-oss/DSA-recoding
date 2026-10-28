"""  

Problem 1: Find the Largest Number in a List

Description

Write a Python function named find_largest(numbers) that takes a list of numbers and returns the largest number in the list.

Constraints

Do not use max().
Do not use sort() or sorted().
If the list is empty, return None.
Aim for O(n) time complexity and O(1) auxiliary space.

Examples

Example 1
Input: [3, 41, 56, 21, 76, 9]
Output: 76
Example 2
Input: [-10, -5, -2, -18]
Output: -2
Example 3
Input: []
Output: None

Hints:

What value could you assume is the largest before checking the rest?
Compare each number with the current largest value.
When you find a larger 
"""

def largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest

Input=[3, 41, 56, 21, 76, 9]
input2 = [-10, -5, -2, -18]
input3 = []

print(largest_number(Input))
print(largest_number(input2))
print(largest_number(input3))