ano = int(input('Digite o ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'ANO: {ano} | Ano bissexto')
else:
    print(f'ANO: {ano} | Ano não-bissexto')
print('--- FIM ---')
