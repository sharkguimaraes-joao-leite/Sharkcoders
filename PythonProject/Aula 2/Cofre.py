#Programa de cofre

banking = True
valores = {"dinheiro" : 0.00, "meta": 5000.00}

def withdraw():
    if valores.get("dinheiro") == 0:
        print("Não pode retirar dinheiro!")
    else:
        try:
            while True:
                retirar = float(input("Quanto dinheiro tenciona retirar?: "))
                if (valores.get("dinheiro") - retirar) < 0:
                    print("Não pode retirar tanto dinheiro!")
                elif retirar < 0:
                    print("Não pode retirar negativo dinheiro!")
                elif retirar == 0:
                    print("Ok, não quer retirar nenhum dinheiro...")
                    break
                else:
                    valores.update({"dinheiro": (valores.get("dinheiro")) - retirar})
                    print(f"Agora, tem {valores.get("dinheiro"):.2f}€ na sua conta!")
                    break
        except ValueError:
            print("Escreva um número")

def deposit():
    while True:
        try:
            depositar = float(input("Quanto dinheiro quer depositar?: "))
            if depositar < 1:
                print("Não pode depositar uma quantidade negativa!")
            else:
                valores.update({"dinheiro": (valores.get("dinheiro")) + depositar})
                break
        except ValueError:
            print("Escreva um número!")

print("Banco de Python!")

while banking:
    if valores.get("dinheiro") >= valores.get("meta"):
        print("Parabéns! Chegou ao seu objetivo!")
        print("Adeus!!")
        banking = False
        break
    else:
        print("****************")
        print("1. Ver dinheiro")
        print("2. Ver meta")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Sair")
        print("****************")
        ação = input("O que quer fazer?: ")
        if ação == "1":
            print(f"Tens {(valores.get("dinheiro")):.2f} depositado!")
        elif ação == "2":
            print(f"Está a {((valores.get("meta")) - (valores.get("dinheiro"))):.2f}€ de chegar ao seu objetivo. Continue!")
        elif ação == "3":
            deposit()
        elif ação == "4":
            withdraw()
        elif ação == "5":
            print("Adeus!!")
            banking = False
            break
        else:
            print("Escolha uma opção invalida (1, 2, 3, 4 ou 5")