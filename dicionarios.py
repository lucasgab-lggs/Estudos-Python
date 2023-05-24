'''Dicionários são estruturas de dados que armazenam pares de elementos,
onde o primeiro elemento é a chave e o segundo é o valor.
Dicionários são representados por chaves {} e os pares de 
elementos são separados por vírgula.'''

# Exemplo 1: Criando um dicionário vazio
dicionario = {} # ou dicionario = dict()
print(dicionario)

print()

# Exemplo 2: Criando um dicionário com elementos
dicionario = {'nome': 'Lucas', 'idade': 20, 'cidade': 'Natal'}
print(dicionario)

print()

# Exemplo 3: Acessando elementos de um dicionário
print(f'Nome: {dicionario["nome"]}')
print(f'Idade: {dicionario["idade"]}')
print(f'Cidade: {dicionario["cidade"]}')

print()

# Exemplo 4: Adicionando elementos em um dicionário
dicionario['sexo'] = 'Masculino'
print(dicionario)

print()

# Exemplo 5: Atualizando elementos de um dicionário
dicionario['idade'] = 21
print(dicionario)

print()

# Exemplo 6: Removendo elementos de um dicionário
del dicionario['sexo']
print(dicionario)

print()

# Exemplo 7: Iterando sobre um dicionário
for chave in dicionario:
    print(f'{chave}: {dicionario[chave]}')

print()

# Exemplo 8: Iterando sobre um dicionário com o método items()
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')

print()

# Exemplo 9: Verificando se uma chave existe em um dicionário
print('nome' in dicionario) # Retorna True
print('peso' in dicionario) # Retorna False

print()

# Exemplo 10: Verificando se um valor existe em um dicionário
print('Lucas' in dicionario.values()) # Retorna True
print('70' in dicionario.values()) # Retorna False
