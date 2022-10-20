from time import sleep
ano = int(input('Olá Jovem. Em qual ano você nasceu?: '))
anoatual = 2022
idade = anoatual-ano
print('Analisando...')
sleep(3.5)
if idade == 18:
    print(f'Você tem {idade} anos. Já está na hora de se alistar!')
elif idade > 18:
    print(f'Você tem {idade} anos. Passaram {idade-18} anos do prazo para se alistar!')
else:
    print(f'Você tem {idade} anos. Faltam {18-idade} anos para o alistamento militar!')
print('Fim do programa!')
