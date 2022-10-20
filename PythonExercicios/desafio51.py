num1 = int(input('Insire um primeiro número: '))
razao = int(input('Insire a razão da PA: '))
cont = num1 + (10-1) * razao
for c in range(0, cont+razao, razao):
    print(c, end=" → ")
print('[ FIM ]')
