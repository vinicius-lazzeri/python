import random
from time import sleep
num1 = int(input('Digite um numero de 0 a 5: '))
num2 = (0, 1, 2, 3, 4, 5)
bingo = random.choice(num2)
print('Processando...')
sleep(3)
if bingo == num1:
    print(f'Você acertou o número sorteado {bingo}, parabéns!')
else:
    print(f'Número sorteado: {bingo}! Seu número: {num1} :S Você errou! Tente novamente!')
print('--FIM--')
