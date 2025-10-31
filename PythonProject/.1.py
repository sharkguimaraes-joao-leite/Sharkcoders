#Jogo de pedra, papel e tesoura
import random
from collections import defaultdict

J = ("pedra", "papel", "tesoura")
W = {"pedra": "tesoura", "papel": "pedra", "tesoura": "papel"}


def ler():
    while True:
        x = input("Pedra / Papel / Tesoura (ou sair): ").strip().lower()
        print("-------------------")
        if x in J or x in ("sair", "q", "exit"):
            return x
        print("Tenta outra vez… (Pedra / Papel / Tesoura)")
        print("-------------------")


def vence(a, b):
    if a == b:
        return "empate"
    return "jogador" if W[a] == b else "computador"

class IA:
    def __init__(self):
        self.freq = defaultdict(int)
        self.trans = defaultdict(lambda: defaultdict(int))
        self.last = None

    def atualizar(self, jog):
        self.freq[jog] += 1
        if self.last is not None:
            self.trans[self.last][jog] += 1
        self.last = jog

    def prever(self):
        if self.last is not None and self.trans[self.last]:
            return max(self.trans[self.last], key=self.trans[self.last].get)
        elif self.freq:
            return max(self.freq, key=self.freq.get)
        else:
            return random.choice(J)

def contra(x):
    for k, v in W.items():
        if v == x:
            return k

def main():
    print("\n=== Pedra-Papel-Tesoura com IA ===\n")
    ia = IA()
    score = {"jogador": 0, "computador": 0, "empate": 0}
    acertos = 0
    tot = 0
    ronda = 1
    while True:
        print(f"\n— Ronda {ronda} —")
        j = ler()
        if j in ("sair", "q", "exit"):
            break
        prev = ia.prever()
        pc = contra(prev)
        res = vence(j, pc)
        tot += 1
        if prev == j:
            acertos += 1
        score[res] += 1
        ia.atualizar(j)
        print(f"Tu: {j} | IA previu: {prev} | PC: {pc}")
        print("Resultado:", "Empate" if res == "empate" else ("Ganhaste" if res == "jogador" else "PC venceu"))
        print(f"Placar Tu:{score['jogador']} PC:{score['computador']} Emp:{score['empate']} | "
              f"Acerto IA: {acertos / tot * 100:.1f}%")
        ronda += 1
    if tot:
        print(f"\nTaxa final de acerto da IA: {acertos / tot * 100:.1f}%")
    print("Até já!")

if __name__ == "__main__":
    main()