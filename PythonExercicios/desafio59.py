from time import sleep
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
op = int(input("""
====================================
Qual operação você deseja realizar?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Escolher outros números
[5] Sair do programa
====================================
→ """))
while op != 5:
    if op == 0 or op > 5:
        op = int(input("""
        ====================================
        Operação inválida! Qual operação você deseja realizar?
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Escolher outros números
        [5] Sair do programa
        ====================================
        → """))
    if op == 1:
        print(f'{num1}+{num2} = {num1+num2}')
        out = str(input('Deseja realizar outra operação? [S/N] → ')).strip().upper()
        if out == 'S':
            op = 4
        elif out == 'N':
            op = 5
        else:
            print('Valor inválido, finalizando o programa...')
            op = 5
    if op == 2:
        print(f'{num1}x{num2} = {num1*num2}')
        out = str(input('Deseja realizar outra operação? [S/N] → ')).strip().upper()
        if out == 'S':
            op = 4
        elif out == 'N':
            op = 5
        else:
            print('Valor inválido, finalizando o programa...')
            op = 5
    if op == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}!')
            sleep(2.5)
            out = str(input('Deseja realizar outra operação? [S/N] → ')).strip().upper()
            if out == 'S':
                op = 4
            elif out == 'N':
                op = 5
            else:
                print('Valor inválido, finalizando o programa...')
                op = 5
        elif num1 == num2:
            print('Os valores são iguais!')
            out = str(input('Deseja realizar outra operação? [S/N] → ')).strip().upper()
            if out == 'S':
                op = 4
            elif out == 'N':
                op = 5
            else:
                print('Valor inválido, finalizando o programa...')
                op = 5
        else:
            print(f'{num2} é maior que {num1}!')
            out = str(input('Deseja realizar outra operação? [S/N] → ')).strip().upper()
            if out == 'S':
                op = 4
            elif out == 'N':
                op = 5
            else:
                print('Valor inválido, finalizando o programa...')
                op = 5
    if op == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        op = int(input("""
====================================
Qual operação você deseja realizar?
[1] Somar
[2] Multiplicar
[3] Maior
[4] Escolher outros números
[5] Sair do programa
====================================
→ """))
    if op == 5:
        print('Finalizando programa...')
    sleep(2.5)
print('[FIM DO PROGRAMA]')
