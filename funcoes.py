'''Funções são blocos de código que podem ser executados 
em qualquer parte do programa. Servem para evitar repetição de código.
São definidas com a palavra reservada def, seguida do nome da função e
entre parênteses os parâmetros de entrada. O bloco de código da função
é definido por indentação. A função pode ou não retornar um valor.
Para retornar um valor, usa-se a palavra reservada return.

Existem algumas funções comuns bem usadas no Python intuitivamente. Como:
print() - imprime na tela
input() - recebe um valor do usuário
len() - retorna o tamanho de uma string ou lista
str() - converte um valor para string
int() - converte um valor para inteiro
float() - converte um valor para float
'''

# Exemplo 1: Função sem parâmetros e sem retorno
def imprime_ola():
    print('Olá Mundo!')
    print('Isto é uma função sem parâmetros e sem retorno')

# Exemplo 2: Função com parâmetros e sem retorno
def imprime_nome(nome):
    print(f'Olá {nome}!')
    print('Isto é uma função com parâmetros e sem retorno')

# Exemplo 3: Função sem parâmetros e com retorno
def retorna_ola():
    print('Isto é uma função sem parâmetros e com retorno')
    return 'Olá Mundo!'

# Exemplo 4: Função com parâmetros e com retorno
def retorna_nome(nome):
    print('Isto é uma função com parâmetros e com retorno')
    return 'Olá ' + nome + '!'

# Utilizando as funções
imprime_ola() # Esta função não retorna nada, apenas imprime na tela
print()
imprime_nome('João') # Esta função não retorna nada, apenas imprime na tela, mas recebe um parâmetro
print()
print(retorna_ola()) # Esta função retorna uma string, que é impressa na tela
print()
print(retorna_nome('Maria')) # Esta função retorna uma string, que é impressa na tela, mas recebe um parâmetro

# Algumas funções mais complexas

# Exemplo 5: Função que recebe dois parâmetros e imprime a soma deles.
def impressao_soma(a, b):
    print(f'A soma de {a} e {b} é igual a {a + b}')

# Exemplo 6: Função que recebe dois parâmetros e retorna a soma deles.
def retorno_soma(a, b):
    print('Esta função retorna a soma de dois números')
    return a + b

# Exemplo 7: Função que pode receber dois parâmetos (nome e sobrenome), mas caso não receba o sobrenome, assume um valor padrão.
def imprime_nome_completo(nome, sobrenome='Silva'):
    print(f'Olá {nome} {sobrenome}!')

# Utilizando as funções
impressao_soma(2, 3) # Esta função não retorna nada, apenas imprime na tela, mas recebe dois parâmetros
print()
print(retorno_soma(2, 3)) # Esta função retorna a soma de dois números, mas recebe dois parâmetros
print()
imprime_nome_completo('João') # Esta função imprime o nome completo na tela com um sobrenome padrão
imprime_nome_completo('João', 'Santos') # Esta função imprime o nome completo na tela com um sobrenome passado como parâmetro
