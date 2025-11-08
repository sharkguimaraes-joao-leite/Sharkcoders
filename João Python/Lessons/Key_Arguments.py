#Keyword Arguments = An argument preceded by an identifier. The order of the arguments doesn't matter.

def hello(greeting, title, first, last):
    print(f"{greeting}, {title} {first} {last}!")

hello(title = "Mr.", last = "Schmoe", greeting = "Hello", first = "Joe")

hello(last = "Dreemurr", first = "Toriel", title = "Ms.",  greeting = "Salutations", )

#If you want to mix positional arguments and keyword ones, make sure the positional ones precede the keyword ones. 

hello("Greetings", "Doctor", last = "James", first ="John")

#There are a lot of hidden keyword arguments in common commands, like the end and separate commands. 
for x in range(1, 11):
    print(x, end = " ")

print()

print("1", "2", "3", "4", "5", sep = "-")

#Exercise 1: Phone Number Generator

def phone_gen(country, first, middle, last):
    return f"{country}-{first}{middle}{last}"

phone_num = phone_gen(country = "+351", middle = 618, last = 171, first = 913)

print(phone_num)