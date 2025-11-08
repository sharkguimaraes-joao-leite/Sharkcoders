#Exceptions = An event that interupts the program, that can be avoided with the try-except method

try:
    number = float(input("Enter a number higher or lower than 0: "))
    div = 1 / number
except ValueError:
    print("Write a number!")
except ZeroDivisionError:
    print("I SAID HIGHER OR LOWER THAN ZERO, YOU SON OF A BIT-")
except Exception:
    print("Something went wrong!")
finally:
    print("Goodbye")

#There are many types of exceptions, each one with its own purpose
#Examples: SyntaxError, ZeroDivisionError, ValueError, TypeError, MethodError,...