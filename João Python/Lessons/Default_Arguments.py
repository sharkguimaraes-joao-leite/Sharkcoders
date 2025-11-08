#Default Arguments = A default value for certain parameters
#Can be used to reduce the number of arguments in a function if a value tends to be the same every time

def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(f"The price of your purchase is {net_price(500):.2f}")
print(f"With your coupon, your price becomes {net_price(500, 0.1)}.")
print(f"Just for you, we will remove the tax, so, your price is {net_price(500, 0.1, 0):.2f}")

#Exercise 1 = Chronometer in Python

import time

while True:
    end = input("How many seconds do you want to wait?: ")
    if end.isdigit() == False:
        print("That value isn't valid. Sneaky bastard...")
    else:
        end = int(end)
        break

def count(end, start = 0):
    for x in range(start, end + 1):
        seconds = int(x) % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    print("Time is up!")

count(end)