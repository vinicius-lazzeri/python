n = int(input('Digite o começo da P.A: '))
p = int(input('Digite o intervalo da P.A: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(n, end=" → ")
        n += p
        c += 1
    print('PAROU PAROU PAROU!')
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f'Progressão finalizada com {total} termos mostrados.')
