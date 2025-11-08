#Logical Operators = evaluate multiple conditions (or, and, not)

#or = at least one condition must be True

temp = 25
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("You probably shouldn't go outside.")
else:
    print(f"You should go outside, it's {temp}ºC.")


#and = both conditions must be True

temp_2 = 28
is_sunny = True

if temp_2 >= 28 and is_sunny:
    print("It's hot outside")
    print("It's sunny!")
    print("It's a beautiful day outside.")
    print("Birds are singing, flowers are blooming.")
    print("On days like these, kids like you...")
    print("Should go on a walk☺️")
    print("What, were you expecting something else?")
elif temp_2 <0 and is_sunny:
    print("It's cold outside")
    print("But it's sunny.")
elif temp_2 < 28 and temp_2 > 0 and is_sunny:
    print("It's warm outside")
    print("And it's sunny. How delightful!")
else:
    print("It's cloudy outside.")


#not = inverts the condition (not False, not True)

temp_3= 28
is_sunny2 = False

if temp_3 >= 28 and not is_sunny2:
    print("It's hot outside")
    print("It's cloudy.")
elif temp_3 <0 and not is_sunny2:
    print("It's cold outside")
    print("And it's cloudy, unfortunate.")
elif temp_3 < 28 and temp_2 > 0 and is_sunny2:
    print("It's warm outside")
    print("But it's cloudy.")
else:
    print("It's sunny outside!")