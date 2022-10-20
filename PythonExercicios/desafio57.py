nome = str(input('Digite seu nome: ')).title()
sexo = str(input('Qual seu sexo? [F/M] ')).upper()
while sexo != 'F' or 'M':
    print(f'Nome {nome} | Sexo: {sexo}')
    nome = str(input('Digite seu nome: ')).title()
    sexo = str(input('Qual seu sexo? [F/M] ')).upper()
    if sexo != 'F' and 'M':
        print('Erro de valor, insira F ou M')
        nome = str(input('Digite seu nome: ')).title()
        sexo = str(input('Qual seu sexo? [F/M] ')).upper()
print('[FIM]')
