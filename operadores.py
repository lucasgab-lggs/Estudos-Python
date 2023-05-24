# Operações matemáticas.
num1 = 10
num2 = 20

print(f'{num1} + {num2} = {num1 + num2}') # Soma.
print(f'{num1} - {num2} = {num1 - num2}') # Subtração.
print(f'{num1} * {num2} = {num1 * num2}') # Multiplicação.

print()

num1 = 20
num2 = 3
print(f'{num1} / {num2} = {num1 / num2}') # Divisão.
print(f'{num1} // {num2} = {num1 // num2}') # Divisão inteira.
print(f'{num1} % {num2} = {num1 % num2}') # Resto da divisão.
print(f'{num1} ** {num2} = {num1 ** num2}') # Potência.

print()

# Operações lógicas.
print(f'{num1} > {num2}: {num1 > num2}') # Maior que (True).
print(f'{num1} < {num2}: {num1 < num2}') # Menor que (False).
print(f'{num1} >= {num2}: {num1 >= num2}') # Maior ou igual a (True).
print(f'{num1} <= {num2}: {num1 <= num2}') # Menor ou igual a (False).
print(f'{num1} == {num2}: {num1 == num2}') # Igual a (False).
print(f'{num1} != {num2}: {num1 != num2}') # Diferente de (True).

print()

# Operações lógicas com strings.
nome1 = 'Lucas'
nome2 = 'Lucas'
print(f'{nome1} == {nome2}: {nome1 == nome2}') # Igual a (True).
print(f'{nome1} != {nome2}: {nome1 != nome2}') # Diferente de (False).

nome1 = 'Lucas'
nome2 = 'lucas'
print(f'{nome1} == {nome2}: {nome1 == nome2}') # Igual a (False).
print(f'{nome1} != {nome2}: {nome1 != nome2}') # Diferente de (True).