from time import sleep
num = int(input('Digite um número: '))
base = str(input('Digite a base de conversão: 1-Binário | 2-Octal | 3-Hexadecimal |: '))
print('Processando...')
sleep(3.5)
if base == '1':
    print(f'{num} Em número binário: {bin(num)[2:]}')
elif base == '2':
    print(f'{num} Em número octal: {oct(num)[2:]}')
elif base == '3':
    print(f'{num} Em número hexadecimal: {hex(num)[2:]}')
else:
    print('Opção Inexiste - Execute o programa novamente.')
print('---FIM DO PROGRAMA---')
