#Feito no Visual Studio Code

while True:
    operador = input("Escolha um operador(+, -, *, /): ")
    print("--------------------------------------------------------")
    if operador == "+" or operador == "-" or operador == "*" or operador == "/":
        break
    else:
        print("Não escolheu um operador válido!")
        print("----------------------------------------------------")

while True:
    num_1 = input("Escreva o primeiro número inteiro: ")
    print("--------------------------------------------------------")
    if num_1.isdigit():
        break
    else:
        print("Não escreveu um número inteiro!")
        print("--------------------------------------------------------")

while True:
    num_2 = input("Escreva o segundo número inteiro: ")
    print("--------------------------------------------------------")
    if num_2.isdigit():
        break
    else:
        print("Não escreveu um número inteiro!")
        print("--------------------------------------------------------")

num_1 = int(num_1)
num_2 = int(num_2)

if operador == "+":
    resultado = num_1 + num_2
elif operador == "-":
    resultado = num_1 - num_2
elif operador == "*":
    resultado = num_1 * num_2
elif operador == "/":
    resultado = num_1 / num_2

if operador == "/":
    print(f"{num_1} {operador} {num_2} = {resultado:.2f}")
else:
    print(f"{num_1} {operador} {num_2} = {resultado}")