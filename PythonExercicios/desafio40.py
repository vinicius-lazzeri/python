nota1 = float(input('Insire a primeira nota: '))
nota2 = float(input('Insire a segunda nota: '))
media = (nota1+nota2)/2
if media < 5:
    print(f'Sua média foi {media}! REPROVADO!')
elif media < 6.9:
    print(f'Sua média foi {media}! RECUPERAÇÃO!')
else:
    print(f'Sua média foi {media}! APROVADO!')
print('Fim do programa!')
