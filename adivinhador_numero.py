'''Importação de bibliotecas necessárias para o funcionamento do jogo.'''
import random

'''Variáveis iniciais para controle do jogo.'''
tentativas = 0
palpite = 0
lim_inferior = int(input('Digite o limite inferior: '))
lim_superior = int(input('Digite o limite superior: '))
numero = random.randint(lim_inferior, lim_superior)

'''Roda um loop até que o usuário acerte o número.'''
while True:
    palpite = int(input('Digite um número para seu palpite: '))
    tentativas += 1

    '''Verifica se os palpites são iguais, menores ou maiores do que o número randomizado.'''
    if palpite == numero:
        print('Parabéns você acertou o número em ', tentativas, ' tentativas.')
        break
    elif palpite < numero:
        print('Você chutou baixo!')
    else:
        print('Você chutou alto!')
        