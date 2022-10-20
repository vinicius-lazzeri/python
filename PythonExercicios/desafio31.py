dist = int(input('Qual distância a ser percorrida? '))
pre1 = dist * 1/2
pre2 = dist * 0.45
if dist <= 200:
    print(f'Distância a ser percorrida: {dist}| Preço à pagar: R${pre1:.2f}')
else:
    print(f'Distância percorrida: {dist}KM| Preço à pagar: R${pre2:.2f}')
print('--- Volte sempre! ---')
