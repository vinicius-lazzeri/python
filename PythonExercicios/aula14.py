n = 1
par = 0
impar = 0
while n != 0:
    n = (int(input('digite um numero: ')))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares.')
