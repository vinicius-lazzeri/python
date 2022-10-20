from datetime import date
date = date.today().year
i = 0
p = 0
for c in range(1, 7+1):
    niver = int(input('Digite o ano do seu nascimento: '))
    if date - niver >= 21:
        i += 1
    else:
        p += 1
print(f'{i} são maiores de idade e {p} são menores de idade.')
