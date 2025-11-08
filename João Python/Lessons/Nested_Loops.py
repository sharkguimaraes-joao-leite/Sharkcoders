#Nested Loops = Loops within another loop (outer, inner)
#               outer loop:
#                   inner loop:

for x in range(3):
    for y in range (1, 10):
       print(y, end = "")
    print()


#Exercise 1 = User generated rectangle

row = int(input("Enter a number of rows: "))
column = int(input("Enter a number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(row):
    for y in range (column):
       print(symbol, end = "")
    print()