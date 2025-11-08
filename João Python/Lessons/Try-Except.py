#Try Except statements = Ways to filter for crashes using the ValueError

while True:
    try:
        num = float(input("Write any number: "))
        print(f"You have {num} days to live.")
        break
    except ValueError:
        print("That ain't a number, partner")

#While this function may seem simple, it's very useful for programs with crash conditions