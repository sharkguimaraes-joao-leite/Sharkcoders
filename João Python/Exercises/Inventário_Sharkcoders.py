#Feito no Visual Studio Code
import time

inventario = list()

while True:
    print(f"Armazenamento: {", ".join(inventario)}")
    print("****************************")
    print("1. Adicionar Item")
    print("2. Retirar Item")
    print("3. Organizar Alfabeticamente")
    print("3. Sair")
    print("****************************")
    act = input("O que queres fazer?: ")
    print("-----------------------")
    match act:
        case "1":
            while True:
                add = input("O que quer adicionar?: ").lower()
                add = add.capitalize()
                print("-----------------------")
                if len(add) > 0:
                    inventario.append(add)
                    print(f"Adicionou {add}")
                    print("-----------------------")
                    break
                else:
                    print("Escreva alguma coisa lol")
                    print("-----------------------")
        case "2":
            while True:
                rem = input("O que quer remover?: ").lower()
                print("-----------------------")
                rem = rem.capitalize()
                if rem in inventario and len(rem) > 0:
                    print(f"Removeu {rem} do armazenamento.")
                    print("-----------------------")
                    inventario.remove(rem)
                    break
                elif len(rem) <= 0:
                    print("Escreva algo lol")
                    print("-----------------------")
                else:
                    print(f"{rem} não está no armazenamento...")
                    print("-----------------------")
        case "3":
            print("Armazenamento organizado!")
            print("-----------------------")
            inventario.sort()
        case "4":
            print("Saindo...")
            time.sleep(1)
            print("-----------------------")
            print("Saiu")
            break
        case _:
            print("Escreva 1, 2, 3 ou 4")
            print("-----------------------")