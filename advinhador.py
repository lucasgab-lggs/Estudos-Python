import random

tentativas = 0
palpite = 0
lim_inferior = int(input("Digite o limite inferior: "))
lim_superior = int(input("Digite o limite superior: "))
numero = random.randint(lim_inferior, lim_superior)

while True:
    palpite = int(input("Digite um número para seu palpite: "))
    tentativas += 1

    if palpite == numero:
        print("Parabéns você acertou o número em ", tentativas, " tentativas.")
        break
    elif palpite < numero:
        print("Você chutou baixo!")
    else:
        print("Você chutou alto!")