""" 
Write a function named list_sum(numbers) that calculates and returns the total of all numbers in a list.
Constraints
Do not use Python's built-in sum() function.
Return 0 for an empty list.
Aim for O(n) time complexity.
Examples
Example 1
Input: [2, 4, 6, 8]
Output: 20
Example 2
Input: [-5, 10, -2]
Output: 3
Example 3
Input: []
Output: 0
Hints
Create a variable that starts at 0.
Visit each number in the list.
Add each number to the value you are keeping.

"""

def list_sum(numbers):
    if not numbers:
        return None
    total = 0  
    for number in numbers:
        total = total + number
    return total  

input1 = [2, 4, 6, 8]
input2 = [-5, 10, -2]
input3 = []


print(list_sum(input1))
print(list_sum(input2))
print(list_sum(input3))