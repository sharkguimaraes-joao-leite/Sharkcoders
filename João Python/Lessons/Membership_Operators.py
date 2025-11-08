#Membership Operators = Used to test whether a value or variable is found in a sequence

secret = "asshole"
guess = []

while True:
    letter = input("Guess a letter in the secret phrase: ").lower()
    print("-------------------------------------------------------")

    if len(letter) > 1:
       print("You wrote more than one character, you can't do that!")
    elif letter in secret and letter in ["a", "e", "i", "o", "u"]:
        if letter in guess:
            print(f"You already guessed {letter}")
        else:
         print(f"There is an {letter} in the word")
         guess.append(letter)
    elif  letter in secret:
        if letter in guess:
            print(f"You already guessed {letter}")
        else:
         print(f"There is a {letter} in the word")
         guess.append(letter)
    elif letter.isalpha() == False:
        print("You didn't write a letter, son of a biscuit!")
    else:
        print(f"{letter} is not in the word. Try again!")
    print("------------------------------------------------------")

    if "a" in guess and "s" in guess and "h" in guess and "o" in guess and "l" in guess and "e" in guess:
       print(f"You got it, the answer is asshole, which is what you are!")
       break

#You can also use membership operators with sets, lists, tuples and dictionaries

students = {"Anne", "Sasha", "Marcy"}

student = input("What student are you searching for: ").lower()
student = student.capitalize()
print("------------------------------------------------------------")

if student in students:
   print(f"{student} was found in our database.")
else:
   print(f"{student} was not found in our database.")
print("------------------------------------------------------------")


grades = {"Anne": "C",
          "Sasha": "B-",
          "Marcy": "A+"}

student = input("Enter the name of one of our students: ").lower()
student = student.capitalize()
print("-------------------------------------------------------------")

if student in grades:
   print(f"{student}'s grade this year was {grades[student]}")
else:
   print(f"{student} was not found in the database")
   print("-----------------------------------------------------------------")

#You can also use the in operator to test if a group of characters is in a string

email = "joaoleite.purpura@gmail.com"

if "@" in email and "." in email:
   print(f"{email} is valid!")
else:
   print(f"{email} is not valid for entry.")