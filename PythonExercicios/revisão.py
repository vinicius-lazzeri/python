media_idade = 0
qtd_mulheres = 0
idade_velho = 0
velho = " "
for c in range(1, 4+1):
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).strip().title()
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media_idade = (idade * c) / 4
    if sexo != 'M' and sexo != 'F':
        print('Execute o programa novamente, de forma adequada dessa vez. M ou F!')
    else:
        if sexo in 'M' and c == 1:
            idade_velho = idade
            velho = nome
            if idade_velho < idade:
                idade_velho = idade
                velho = nome
        if sexo == 'F' and idade < 20:
            qtd_mulheres += 1
print(f'Média de idade do grupo: {media_idade} anos')
print(f'Nome do homem mais velho: {velho}')
print(f'Total de mulheres com menos de 20 anos? {qtd_mulheres}.')

