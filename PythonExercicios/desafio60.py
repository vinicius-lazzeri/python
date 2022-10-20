num = int(input('Digite um número inteiro qualquer: '))
c = num
fat = 1
while c > 0:
    if c <= 1:
        print(c, end=" = ")
    else:
        print(c, end=" x ")
    fat *= c
    c -= 1
print(fat)