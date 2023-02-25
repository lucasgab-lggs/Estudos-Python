'''Importação de bibliotecas necessárias para o funcionamento do jogo.'''
import random

'''Variáveis iniciais para controle do jogo.'''
palavras = ["casa", "cachorro", "carro", "elefante",
            "computador", "ciencia", "vidro", "luz",
            "biblioteca", "tesoura", "secador", "mesa"]
palavra = random.choice(palavras)
tentativas = ""
turnos = 12

print("Descubra as letras da palavra e revele-a!")

'''Loop até que o usuário esgote as 12 tentativas'''
while turnos > 0:

    '''Contador que indica a quantidade de letras não descobertas'''
    restantes = 0

    '''Loop para impressão (ou não) das letras que já foram descobertas'''
    for letra in palavra:
        if letra in tentativas:
            print(letra)
        else:
            print("-")
            restantes += 1
    
    '''Verifica se o usuário descobriu todas as letras que tinha para descobrir'''
    if restantes == 0:
        print("Você venceu!")
        print("A palavra era:", palavra)
        break
    
    '''Recebimento de entrada para o palpite do usuário'''
    tentativa = input("Qual letra? ")
    tentativas += tentativa

    '''Verifica se a letra digitada NÃO se encontra na palavra escolhida'''
    if tentativa not in palavra:
        turnos -= 1
        print("Errado!")
        print("Você tem mais", turnos, "tentativas!")
        if turnos == 0:
            print("Você perdeu!")
