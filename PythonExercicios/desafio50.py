s = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite valores inteiros: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Vc digitou {cont} números pares e a soma dos valores é igual a {s}')
print('Fim do programa')
