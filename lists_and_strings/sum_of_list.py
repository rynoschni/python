numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6]

print(sum(numbers))
print(max(numbers))
print(min(numbers))

# Even Numbers
for number in numbers:
    if (number % 2) == 0:
        print(number)

# Odd Numbers
for number in numbers:
    if (number % 2) != 0:
        print(number)

positive_numbers = []
for number in numbers:

    if (number > 0):
        positive_numbers.append(number)
print(positive_numbers)


positive_numbers_2 = []
for number in numbers:

    if (number >= 0):
        positive_numbers_2.append(number)
print(positive_numbers_2)
