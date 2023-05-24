'''Listas são estruturas de dados que podem ser alteradas, ou seja, são mutáveis.
São definidas por colchetes [] e seus elementos são separados por vírgula.
As listas podem conter elementos de diferentes tipos, inclusive outras listas.'''

lista_nome = ['João', 'Maria']
lista = [1, 'dois', 3.0, True, lista_nome]

def imprime_lista(lista):
    print(f'Tamanho da lista: {len(lista)}')
    print(f'Lista: {lista}')
    print()

# Imprimindo a lista
imprime_lista(lista)

# Acessando elementos da lista
print(lista[0])

# Acessando elementos da lista dentro de outra lista
print(lista[4][0])

# Acessando último elemento da lista
print(lista[-1])

# Acessando penúltimo elemento da lista
print(lista[-2])

# Acessando elementos da lista com fatiamento
print(lista[0:2]) # Imprime do elemento 0 ao 1

# Acessando elementos da lista com fatiamento
print(lista[2:]) # Imprime do elemento 2 ao último

# Acessando elementos da lista com fatiamento
print(lista[:2]) # Imprime do primeiro elemento ao elemento 1

# Acessando elementos da lista com fatiamento
print(lista[::2]) # Imprime do primeiro elemento ao último, pulando de 2 em 2

# Acessando elementos da lista com fatiamento
print(lista[::-1]) # Imprime do último elemento ao primeiro, pulando de 1 em 1

# Alterando elementos da lista
lista[0] = 'um'

# Imprimindo a lista
imprime_lista(lista)

# Formas de criar uma lista.
lista1 = list()
lista2 = []

# Criando uma lista com range
lista3 = list(range(10))

# Criando uma lista com range e passo
lista4 = list(range(0, 10, 2))

# Criando uma lista com range e passo negativo
lista5 = list(range(10, 0, -1))

# Imprimindo as listas
imprime_lista(lista1)
imprime_lista(lista2)
imprime_lista(lista3)
imprime_lista(lista4)
imprime_lista(lista5)

# Métodos de lista
minha_lista = [1, 2, 3, 4]
imprime_lista(minha_lista)

# Append - Adiciona um elemento no final da lista.
print('Adicionando o número 5 no final da lista.')
minha_lista.append(5)

# Imprimindo a lista
imprime_lista(minha_lista)

# Extend - Adiciona uma lista no final da lista.
print('Adicionando os números 6, 7, 8 e 9 no final da lista.')
minha_lista.extend([6, 7, 8, 9])

# Imprimindo a lista
imprime_lista(minha_lista)

# Insert - Adiciona um elemento em uma posição específica da lista.
print('Adicionando o número 0 na posição 0 da lista.')
minha_lista.insert(0, 0)

# Imprimindo a lista
imprime_lista(minha_lista)

# Remove - Remove o primeiro elemento da lista que seja igual ao elemento passado como parâmetro
print('Removendo o número 0 da lista.')
minha_lista.remove(0)

# Imprimindo a lista
imprime_lista(minha_lista)

# Adicionando elementos repetidos na lista.
print('Adicionando o número 1 na lista.')
minha_lista.append(1)

# Imprimindo a lista
imprime_lista(minha_lista)

# Count - Conta quantas vezes um elemento aparece na lista.
print(f'O número 1 aparece {minha_lista.count(1)} vezes na lista.')

# Index - Retorna o índice do primeiro elemento da lista que seja igual ao elemento passado como parâmetro.
print(f'O número 1 aparece pela primeira vez na posição {minha_lista.index(1)} da lista.')

print()

# Sort - Ordena a lista.
print('Ordenando a lista inversamente.')
minha_lista.sort(reverse=True)

# Imprimindo a lista
imprime_lista(minha_lista)

# Sum - Soma todos os elementos da lista.
print(f'A soma dos elementos da lista é {sum(minha_lista)}.')

# Max - Retorna o maior elemento da lista.
print(f'O maior elemento da lista é {max(minha_lista)}.')

# Min - Retorna o menor elemento da lista.
print(f'O menor elemento da lista é {min(minha_lista)}.')
