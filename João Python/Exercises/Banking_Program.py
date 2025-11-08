#Exercise  = Python Banking Program

dep = 0
wit = 0
money = 2000
money = float(f"{money:.2f}")

banking = True

def balance(money):
    print(f"You have {money}€ ")

def deposit(money, dep):
    money = money + dep
    print(f"You now have {money}€ in your bank account")

def withdraw(money, wit):
    money = money - wit
    print(f"You now have {money}€ in your bank account")

while banking == True:
    print("***************")
    print("Banking Program")
    print("***************")
    print("1. Show Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("-----------------")
    while True:
        act = input("What would you like to do (type 1, 2, 3 or 4): ")
        if act == "1" or act == "2" or act == "3" or act == "4":
            break
        else:
            print("Not an option")
    if act == "1":
        balance(f"{money:.02f}")
    elif act == "2":
        while True:
            try:
                dep = float(input("How much money would you like to deposit?: "))
                print("---------------------------------------")
                break
            except ValueError:
                print("You didn't write a valid number.") 
                print("----------------------------------------")
        dep = float(f"{dep:.2f}")
        deposit(money, dep)
        money += dep
    elif act == "3":
        while True:
            try:
                wit = float(input("How much money would you like to withdraw?: "))
                print("---------------------------------------")
                break
            except ValueError:
                print("You didn't write a valid number.") 
                print("----------------------------------------")
        wit = float(f"{wit:.2f}")
        withdraw(money, wit)
        money -= wit
    else:
        print("Thank you for doing business with us!")
        banking == False
        break