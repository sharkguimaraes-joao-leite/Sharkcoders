#Programa para fazer contas de quizzes com pontuação

points = 0.0

while True:
    ques_num = input("How many questions does your quiz have?: ")
    print("-------------------------------------------------")
    if ques_num.isdigit() == False:
        print("Please take this seriously, asshole")
        print("-------------------------------------------------")
    else:
        break

ques_num = int(ques_num)

for x in range(1, ques_num + 1):
    while True:
        try:
            add = float(input(f"How many points did you get on your {x}º question?: "))
            print("-------------------------------------------------")
            points = points + add
            break
        except ValueError:
            print("Please write a valid number")
            print("-------------------------------------------------")

print(f"You got {points:.2f} points!")