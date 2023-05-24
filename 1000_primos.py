lista = []
i = 0

def primo(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

while len(lista) < 1000:
    if (primo(i)) == True:
        lista.append(i)
    i += 1

for j in range(0, len(lista)):
    print(f"[{j+1}] = {lista[j]}")