somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 4+1):
    print('-' * 4, f'{p} Pessoa', '-' * 4)
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade> maioridadehomem:
        maioridade = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'Média de idade do grupo: {mediaidade}')
print(f'Nome do homem mais velho: {nomevelho}')
print(f'Quantidade de mulheres menos de 20 anos: {totmulher20}')
