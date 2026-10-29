""" 
Problem 2: Find the Smallest Number in a List
Description
Write a function named find_smallest(numbers) that returns the smallest number in a list.
Constraints
Do not use min().
Do not sort the list.
Return None if the list is empty.
Aim for O(n) time complexity.
Examples
Example 1
Input: [8, 3, 12, 1, 7]
Output: 1
Example 2
Input: [-3, -10, -1, -6]
Output: -10
Hints
Start by remembering one number from the list.
Visit every other number.
Ask: "Is this number smaller than the smallest one I have seen?"

"""

def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for m in numbers:
        if m < smallest:
            smallest = m
    return smallest

input1 = [8, 3, 12, 1, 7]
input2 = [-3, -10, -1, -6]
input3 = []

print(find_smallest(input1))
print(find_smallest(input2))
print(find_smallest(input3))