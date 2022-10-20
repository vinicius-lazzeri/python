nome = str(input('Digite seu nome: ')).strip()
dividido = nome.split()
print(f'Seu nome em letras maísculas: {nome.upper()}| em letras minúsculas: {nome.lower()}|')
print(f'Total de letras sem espaços: {len(nome.replace(" ", ""))}| Qtd de letras no primeiro nome:{len(dividido[0])}')
