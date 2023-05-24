'''Conversão de tipos de dados em Python.
    int() - Converte para inteiro.
    float() - Converte para float.
    str() - Converte para string.
    bool() - Converte para booleano.
    
    Obs.: O método input() sempre retorna uma string. Pode-se, 
    então, converter o valor retornado para o tipo desejado.
'''

numero1 = '10'
numero2 = '30'
print(f"'{numero1}' ({type(numero1)})") # <class 'str'>
print(f"'{numero2}' ({type(numero2)})") # <class 'str'>
print(f"'{numero1}' + '{numero2}' = {numero1 + numero2}") # 1030 (Concatenção de strings).

print()
numero1 = int(numero1) # Converte a string '10' para o inteiro 10.
numero2 = int(numero2) # Converte a string '30' para o inteiro 30.
print(f'{numero1} ({type(numero1)})') # <class 'int'>
print(f'{numero2} ({type(numero2)})') # <class 'int'>
print(f'{numero1} + {numero2} = {numero1 + numero2}') # 40 (Soma de inteiros).

print()
numero1 = float(numero1) # Converte o inteiro 10 para o float 10.0.
numero2 = float(numero2) # Converte o inteiro 30 para o float 30.0.
print(f'{numero1} ({type(numero1)})') # <class 'float'>
print(f'{numero2} ({type(numero2)})') # <class 'float'>
print(f'{numero1} + {numero2} = {numero1 + numero2}') # 40.0 (Soma de floats).

print()

numero1 = str(numero1) # Converte o float 10.0 para a string '10.0'.
numero2 = str(numero2) # Converte o float 30.0 para a string '30.0'.
print(f"'{numero1}' ({type(numero1)})") # <class 'str'>
print(f"'{numero2}' ({type(numero2)})") # <class 'str'>
print(f"'{numero1}' + '{numero2}' = {numero1 + numero2}") # 10.030 (Concatenção de strings).

print()
verdadeiro = 1
falso = 0
print(f'Verdadeiro: {verdadeiro} ({type(verdadeiro)})') # <class 'int'>
print(f'Falso: {falso} ({type(falso)})') # <class 'int'>
verdadeiro = bool(verdadeiro) # Converte o inteiro 1 para o booleano True.
falso = bool(falso) # Converte o inteiro 0 para o booleano False.
print(f'Verdadeiro: {verdadeiro} ({type(verdadeiro)})') # <class 'bool'>
print(f'Falso: {falso} ({type(falso)})') # <class 'bool'>
