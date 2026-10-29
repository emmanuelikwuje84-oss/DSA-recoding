def count_even(numbers):
    if not numbers:
        return None

    total = numbers[0]
    for number in numbers:
        if number % 2 == 0:
            total = number
    return total // 2

input1 = [1, 2, 3, 4, 6]
input2 = [1, 3, 5, 7]
input3 = []

print(count_even(input1))
print(count_even(input2))
print(count_even(input3))