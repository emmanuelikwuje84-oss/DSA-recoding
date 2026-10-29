def count_occurrences(numbers, target):
    if not numbers:
        return  None

    counter = 0

    for number in numbers:
        if number == target:
            counter = counter +1
    return counter


input1 = [2, 5, 2, 8, 2] 
target1 = 2
input2 = [1, 4, 7] 
target2 = 10

print(count_occurrences(input1,target1))
print(count_occurrences(input2,target2))          