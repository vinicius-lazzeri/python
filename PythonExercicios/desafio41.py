from time import sleep
from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
anoatual = date.today().year
idade = anoatual-ano
print('Analisando para determinar sua categoria de competição...')
sleep(3.5)
if idade <= 9:
    print(f'Você tem {idade} anos de idade. Você é MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos de idade. Você é INFANTIL')
elif idade <= 19:
    print(f'Você tem {idade} anos de idade. Você é JUNIOR')
elif idade == 20:
    print(f'Você tem {idade} anos de idade. Você é SÊNIOR')
else:
    print(f'Você tem {idade} anos de idade. Você é MASTER')
print('---FIM DO PROGRAMA---')
