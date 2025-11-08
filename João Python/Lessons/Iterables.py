#Iterables = An object or collection that can return its elements one at a time

set = {2, 5, 3, 7}

for num in set:
    print(num, end = " ")

print("-----------------------------------------------")

str = "João Henrique"

for chara in str:
    print(chara)

print("-----------------------------------------------")

dict = {"A": 1, "B": 2, "C": 3}

for key, value in dict.items():
    print(f"{key} = {value}")