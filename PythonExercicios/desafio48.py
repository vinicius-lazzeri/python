s = 0
cont = 0
for c in range(1, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            cont += 1
            s += c
print(f'A soma entre todos os {cont} números ímpares de 1-500 divisíveis por 3 é: {s}')
