salario = float(input('Qual seu salário? '))
if salario > 1250:
    print(f'Salário: R${salario:.2f}| Salário com aumento de 10%: R$ {salario+(salario*(10/100)):.2f}')
else:
    print(f'Salário: R${salario:.2f}| Salário com aumento de 15%: R$ {salario+(salario*(15/100)):.2f}')
print('Continue com seu bom trabalho!')
