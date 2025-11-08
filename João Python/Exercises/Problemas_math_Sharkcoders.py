#Feito no Visual Studio Code
import math
import time
running = True

def escolha_1():
    primo = True
    while True:
                try:
                    num = int(input("Que número quer determinar se é primo?: "))
                    print("------------------------------------------------")
                    num_sqrt = math.sqrt(num)
                    bla = math.ceil(num_sqrt)
                    for x in range(2, bla):
                        div = num / x
                        if div == int(div):
                            primo = False
                            break
                        elif num == 1|0 or num < 0:
                             primo = False
                        else:
                            primo = True
                    if primo == False:
                        print(f"{num} não é primo.")
                    else:
                        print(f"{num} é primo!")
                except ValueError:
                    print("Por favor escreva um número válido")
                break
def escolha_2():
     fator = 0
     while True:
          try:
               num = int(input("Que número quer descobrir o seu fatorial?: "))
               print("---------------------------------------------")
               if num == 0:
                    print("O fatorial de 0 é 1.")
                    break
               elif num < 0:
                    print("Um número negativo não é válido!")
                    print("---------------------------------------------")
               else:
                    fator = num
                    for x in range(1, num):
                         fator = fator * (num - x)
                    print(f"O fatorial de {num} é {fator}")
                    break
          except ValueError:
               print("Não Válido")

def escolha_3():
     while True:
          try:
               num = int(input("Até que número quer contar?: "))
               print("---------------------------------------------")
               if num <= 0:
                    print("Escreva um número válido")
                    print("---------------------------------------------")
               else:
                    for x in range(1, num + 1):
                         print(x)
                         time.sleep(0.333333)
                    print("Acabou!")
                    print("---------------------------------------------")
                    break
          except ValueError:
               print("Por favor escreva um número válido")
               print("---------------------------------------------")


while running:
    num = 0
    print("****************************")
    print("1. Determinar números primos")
    print("2. Calcular fatoriais")
    print("3. Contar até um número")
    print("4. Sair")
    print("****************************")
    escolha = input("O que quer fazer?: ")
    print("------------------------------")  
    if escolha == "1" or escolha == "2" or escolha == "3" or escolha == "4":
        if escolha == "1":
             escolha_1()
        elif escolha == "2":
             escolha_2()
        elif escolha == "3":
             escolha_3()
        else:
             print("Adeus!")
             running = False
             break
    else:
        print("Não é uma escolha válida")