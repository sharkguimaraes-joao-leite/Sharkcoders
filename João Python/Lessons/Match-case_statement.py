#Match-case Statement (switch) = An alternative to using many elif statements

def day_week(day):
    match day:
        case 1:
            return "It's monday"
        case 2:
            return "It's tuesday"
        case 3:
            return "It's wednesday"
        case 4:
            return "It's thursday"
        case 5:
            return "It's friday"
        case 6:
            return "It's saturday"
        case 7:
            return "It's sunday"
        case _:
            return "Not Valid"
    
print(day_week(7))

#To create else statements in match-case statementsm use case _
#You can use | to substitute for an or statement

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Not Valid"

day = input("What day of the week is it: ").lower()
day = day.capitalize()

if is_weekend(day) == "Not Valid":
    print("You didn't write a day of the week, asshole!")
elif is_weekend(day) == False:
    print("It's not weekend. Bummer...")
else:
    print("It's weekend!")
