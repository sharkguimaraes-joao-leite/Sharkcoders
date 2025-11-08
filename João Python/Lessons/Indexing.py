#Indexing = Accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]


#Start & End = Identify a character in a string

credit_number = "1029-3847-4651-0293"

print(credit_number[0])

#Note = If you have only 1 field listed, without any colons, it assumes it is a "start"


#How to identify a group of characters in a string [a:b]

print(credit_number[0:4])
print(credit_number[6:10])
print(credit_number[:6])
print(credit_number[8:])
print(credit_number[-1])

last_digits = credit_number[15:]
print(f"The last digits of your credit card are {last_digits}.")

#Note = The "start" operator is inclusive (includes the character), but the "end" operator is exclusive (excludes the character)
#Note = If you exclude the "start" operator will start in the first character of the string, and the "end" operator will end in the last character.
#Note = If your index is a negative number, the character shown will be counted starting from the last character of your string


#Step = Show characters in a sequence of intervals

print(credit_number[::3])

#Note = Using an index value in the negatives will reverse the string

credit_number = credit_number[::-1]
print(credit_number)