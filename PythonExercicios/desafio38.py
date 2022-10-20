from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('-=--=--=- Analisando... -=--=--=-')
sleep(3.5)
if num1 > num2:
    print(f'O primeiro valor {num1} é maior que o segundo valor {num2}!')
elif num2 > num1:
    print(f'O segundo valor {num2} é maior que o primeiro valor {num1}!')
else:
    print('Não existe valor maior, os dois são iguais.')
print('-=--=--=- FIM DO PROGRAMA -=--=--=-')
