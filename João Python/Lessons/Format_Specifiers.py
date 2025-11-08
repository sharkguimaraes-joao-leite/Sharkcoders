#Format Specifiers = Flags that format a value based on whose are inserted (value:flags)

price_1 = 3.8729
price_2 = 78.65964
price_3 = 12.3563

# .(number)f = Round to that many decimal places (fixed point)

print(f"The first price is ${price_1:.2f}")
print(f"The second price is ${price_2:.2f}")
print(f"The third price is ${price_3:.2f}")


# :(number) = Allocate that many spaces

print(f"The first price is {price_1:10}")
print(f"The second price is {price_2:10}")
print(f"The third price is {price_3:10}")


# :0(number) = Allocate and zero pad that many spaces

print(f"The first price is {price_1:010}")
print(f"The second price is {price_2:010}")
print(f"The third price is {price_3:010}")


# :< = Left justify

print(f"The first price is {price_1:<10}")
print(f"The second price is {price_2:<10}")
print(f"The third price is {price_3:<10}")


# :> = Right justify

print(f"The first price is {price_1:>10}")
print(f"The second price is {price_2:>10}")
print(f"The third price is {price_3:>10}")


# :^ = Center align

print(f"The first price is {price_1:^10}")
print(f"The second price is {price_2:^10}")
print(f"The third price is {price_3:^10}")


# :+ = Use a plus sign to indicate positive values

print(f"The first price is {price_1:+}")
print(f"The second price is {price_2:+}")
print(f"The third price is {price_3:+}")


# :  = Insert a space before positive numbers

print(f"The first price is {price_1: }")
print(f"The second price is {price_2: }")
print(f"The third price is {price_3: }")


# := = Place a sign to the leftmost position

print(f"The first price is {price_1:=10}")
print(f"The second price is {price_2:=10}")
print(f"The third price is {price_3:=10}")


# :, = Comma separator

price_1 += 1000
price_2 += 1000
price_3 += 1000
print(f"The first price is {price_1:,}")
print(f"The second price is {price_2:,}")
print(f"The third price is {price_3:,}")

#You can also combine flags with one another

print(f"The first price is {price_1:,.2f}")
print(f"The second price is {price_2:,.2f}")
print(f"The third price is {price_3:,.2f}")