#List Comprehension = A concise way to create lists in Python
#You can use the formula [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]

print(doubles)
print("--------------------------------------------------")

triples = [y * 3 for y in range(1, 11)]

print(triples)
print("--------------------------------------------------")

squares = [z * z for z in range(1, 11)]

print(squares)
print("--------------------------------------------------")

#You can also use list comprehension with lists of values

fruits = ["apple", "orange", "banana", "peach"]
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)
print("--------------------------------------------------")

nums = [4, -2, -9, 0, 1, 8, 3, -5, 6]

plus_nums = [num for num in nums if num > 0]
print(plus_nums)
print("--------------------------------------------------")

minus_nums = [num for num in nums if num < 0]
print(minus_nums)
print("--------------------------------------------------")

even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)
print("--------------------------------------------------")

odd_nums = [num for num in nums if num % 2 == 1]
print(odd_nums)
print("--------------------------------------------------")


grades = [85, 62, 45, 23, 91, 36]
passing_grades = [grade for grade in grades if grade >= 50]
print(passing_grades)