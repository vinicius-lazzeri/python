num1 = int(input('Escolha um número para você ver a tabuada 1-10 deste número: '))
for c in range(1, 10+1, 1):
    n2 = num1 * c
    print(f'{c} x {num1} = {n2}')
print('Fim do programa')
