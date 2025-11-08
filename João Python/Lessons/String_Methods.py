#Length Function = used to measure the length of a string
name = input("Please enter your full name: ")

result = len(name)

print(f"Hello {name}! Your name is {result} characters long.")

#Find Function = used to identify the first occurence of a given character in a string
#Note = The first character in a string has a value of 0 instead of 1

result_2 = name.find("o")

if name.find("o") == -1:
   print("Your name doesn't have any 'o' in it")
else:
   print(f"The first occurence of the letter 'o' in your name is in the position {result_2}.")


#rFind Function = used to identify the last occurence of a given character in a string

result_3 = name.rfind("e")

if name.rfind("e") == -1:
   print("Your name doesn't have any 'e' in it")
else:
   print(f"The last occurence of the letter 'e' in your name is in the position ")


#Capitalize() = Makes the first letter of a string upper-case

name = name.capitalize()
print(name)


#Upper() & Lower() = Makes all characters upper-case and lower-case

name = name.upper()
print(name)

name = name.lower()
print(name)


#IsDigit() = Returns a signal of True or False if the string only contains digits (numbers)

result_4 = name.isdigit()
print(result_4)


#IsAlpha() = Returns a signal of True or False if the string only contains alphabetical characters (letters)

result_5 = name.isalpha()
print(result_5)

#Note: Spaces don't qualify as either digits or letters, so a string with spaces will give a False signal


#Count = Counts the number of a character is a string

phone_number = input("What is your phone number?: ")
dash = phone_number.count("-")

print(dash)


#Replace = Replaces any character with another character

phone_number = phone_number.replace("-", "")
print(phone_number)


#For more commands with the string variable, type print(help(str))