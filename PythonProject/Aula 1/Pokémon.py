#Feito no Sharkcoders como um exercicio
import random
import time

chance = (1, 2, 3, 4, 5)
battle = True
print("************************")
print("A wild Caterpie appeared")
while battle:
    print("1. Battle")
    print("2. Catch")
    print("3. Item")
    print("4. Run")
    escolha = input("What will you do? ")
    if escolha == "1" or escolha == "2" or escolha == "3" or escolha == "4":
        if escolha == "1":
            while True:
                print("1. Ember")
                print("2. Tackle")
                print("3. Fire Fang")
                print("4. Scratch")
                ataque = input("What will Charmander do? ")
                if ataque == "1" or ataque == "2" or ataque == "3" or ataque == "4":
                    if ataque == "1":
                        print("It's supereffective!")
                        print("Caterpie fainted.")
                        print("You won the battle!")
                        battle = False
                    elif ataque == "2":
                        print("Caterpie fainted.")
                        print("You won the battle!")
                        battle = False
                    elif ataque == "3":
                        print("It's supereffective!")
                        print("Caterpie fainted.")
                        print("You won the battle!")
                        battle = False
                    else:
                        print("Caterpie fainted.")
                        print("You won the battle!")
                        battle = False
                    break
                else:
                    print("Not an option")
        elif escolha == "2":
            print("You threw a Pokéball")
            print("...")
            time.sleep(1)
            lol = random.randint(1,5)
            if lol < 5:
                print("You caught a Caterpie yay!")
                battle = False
                break
            else:
                print("The Pokémon escaped from the ball!")
        elif escolha == "3":
            print("You used a potion.")
            print("Your Pokémon healed 20 HP")
        else:
            print("You ran away!")
            battle = False
            break
    else:
        print("Not an option!")