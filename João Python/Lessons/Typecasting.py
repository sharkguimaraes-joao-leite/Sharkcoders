 #Typecasting = the process of converting a variable from one data type to another

name = "João Henrique"
age = 14
gpa = 4.5
is_student = True
#To know a data type of a variable, run the type function inside a print function, like "print(type(name))"

gpa = int(gpa)
age = float(age)
name = bool(name)

print(gpa)
print(age)
print(name)
#If a str is converted into a bool, that makes it so that it checks if there exists a variable "name" or not
#User imput is always a str, so this function is useful if you wanna convert it into a int, float or bool