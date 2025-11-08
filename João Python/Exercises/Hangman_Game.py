#Hangman game for practise
import random

#Values
words_easy = ("ananas", "pizza", "planeta", "peixe", "video", "camisola", "manta", "consola", "painel",
              "ratazana", "teclado", "borboleta", "guaxinim", "doninha", "elefante", "tigre", "mochila",
              "esfera", "nuvem", "marte", "arvore", "banana", "melao", "carne", "panqueca", "esquilo",
              "massa", "abacate", "polvo", "churrasco")
words_hard = ("cristianismo", "computador", "dinamarques", "singapura", "armazenamento",
              "pneumoultramicroscopicosilicovulcanoconiose", "pistola", "atmosfera", "sanguineo",
              "comboio", "planetario", "femenismo", "genocidio", "hipermercado", "agradecimento",
              "antidepressivos", "mercadoria", "impressora", "eletronico", "medicamento", "melancia",
              "engenheiro", "contabilista", "frigorifico", "dicionario", "televisao", "masculinidade",
              "obtuso", "tiranossaurus", "apartamento")
answer_easy = random.choice(words_easy)
hint_easy = ["_"] * len(answer_easy)
answer_hard = random.choice(words_hard)
hint_hard = ["_"] * len(answer_hard)
wrong_guess = 0
guess_letters = set()
playing = True
used = []
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

#Functions
def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)

def display_hint_easy(hint_easy):
    print(" ".join(hint_easy))

def display_hint_hard(hint_hard):
    print(" ".join(hint_hard))

def display_ans_easy(answer_easy):
    print(" ".join(answer_easy))

def display_ans_hard(answer_hard):
    print(" ".join(answer_hard))

#Main Code
print("Jogo da Forca!")
print("*******")
print("1. Fácil")
print("2. Difícil")
print("*******")
while True:
    dif = input("Que dificuldade quer selecionar?: ")
    if dif == "1" or dif == "2":
        break
    else:
        print("Escreva 1 ou 2!")
while playing:
    if dif == "1":
        print("********")
        display_man(wrong_guess)
        print("********")
        display_hint_easy(hint_easy)
        while True:
            guess = input("Escreva uma letra: ").lower()
            if guess.isalpha() and len(guess) == 1:
                break
            elif guess in used:
                print(f"You already guessed {guess}")
            else:
                print("Esreva uma letra!")
        if guess in answer_easy:
            print("Correto!")
            for i in range(len(answer_easy)):
                if answer_easy[i] == guess:
                    hint_easy[i] = guess
                else:
                    pass
        else:
            print("ERRADO!")
            wrong_guess += 1
        used.append(guess)
        if wrong_guess >= 6:
            print("********")
            display_man(wrong_guess)
            print("********")
            print("Perdeste...")
            print(f"A palavra era {answer_easy}")
            while True:
                play = input("Jogar de-novo (y/n)?: ").lower()
                if play == "y":
                    print("OK!")
                    answer_easy = random.choice(words_easy)
                    hint_easy = ["_"] * len(answer_easy)
                    answer_hard = random.choice(words_hard)
                    hint_hard = ["_"] * len(answer_hard)
                    wrong_guess = 0
                    guess_letters = set()
                    playing = True
                    used = []
                    break
                elif play == "n":
                    print("Adeus...")
                    playing = False
                    break
                else:
                    print("Escreva y ou n")
        else:
            pass
        if "_" not in hint_easy:
            print("Parabéns! Ganhaste!")
            print(f"A palavra era", answer_easy.capitalize())
            while True:
                play = input("Jogar de-novo (y/n)?: ").lower()
                if play == "y":
                    print("OK!")
                    answer_easy = random.choice(words_easy)
                    hint_easy = ["_"] * len(answer_easy)
                    answer_hard = random.choice(words_hard)
                    hint_hard = ["_"] * len(answer_hard)
                    wrong_guess = 0
                    guess_letters = set()
                    playing = True
                    used = []
                    break
                elif play == "n":
                    print("Adeus...")
                    playing = False
                    break
                else:
                    print("Escreva y ou n")
        else:
            pass
    else:
        print("********")
        display_man(wrong_guess)
        print("********")
        display_hint_hard(hint_hard)
        while True:
            guess = input("Escreva uma letra: ").lower()
            if guess.isalpha() and len(guess) == 1:
                break
            else:
                print("Escreva uma letra!")
        if guess in answer_hard:
            print("Correto!")
            for i in range(len(answer_hard)):
                if answer_hard[i] == guess:
                    hint_hard[i] = guess
                else:
                    pass
        else:
            print("ERRADO!")
            wrong_guess += 1
        used = []
        if wrong_guess >= 6:
            print("********")
            display_man(wrong_guess)
            print("********")
            print("Perdeste...")
            print(f"A palavra era {answer_hard}")
            while True:
                play = input("Jogar de-novo (y/n)?: ").lower()
                if play == "y":
                    print("OK!")
                    answer_easy = random.choice(words_easy)
                    hint_easy = ["_"] * len(answer_easy)
                    answer_hard = random.choice(words_hard)
                    hint_hard = ["_"] * len(answer_hard)
                    wrong_guess = 0
                    guess_letters = set()
                    playing = True
                    used = []
                    break
                elif play == "n":
                    print("Adeus...")
                    playing = False
                    break
                else:
                    print("Escreva y ou n")
        else:
            pass
        if "_" not in hint_hard:
            print("Parabéns! Ganhaste!")
            print(f"A palavra era", answer_hard.capitalize())
            while True:
                play = input("Jogar de-novo (y/n)?: ").lower()
                if play == "y":
                    print("OK!")
                    answer_easy = random.choice(words_easy)
                    hint_easy = ["_"] * len(answer_easy)
                    answer_hard = random.choice(words_hard)
                    hint_hard = ["_"] * len(answer_hard)
                    wrong_guess = 0
                    guess_letters = set()
                    playing = True
                    used = []
                    break
                elif play == "n":
                    print("Adeus...")
                    playing = False
                    break
                else:
                    print("Ecreva y ou n")
    