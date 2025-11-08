#Conditional Expressions = A one-line shortcut for the if-else statement ((also known as the ternary operator))
#                          Print or assign one of two values based on a condition
#                          Return "X" if condition, else return "Y"

num = 5
num_2 = 7

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)

max_num = num if num > num_2 else num_2
min_num = num if num < num_2 else num_2
print(f"The bigger number is {max_num}, and the lower number in {min_num}")


age = 14
status = "You're an adult!" if age >= 18 else "You're a child."
print(status)


temp = 35
weather = "Hot" if temp >=30 else "Cold"
print(weather)


user_role = "admin"
access_level = "You have full access" if user_role == "admin" else "You have limited access"
print(access_level)