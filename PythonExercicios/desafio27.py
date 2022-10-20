nome = str(input('Insire seu nome completo: '))
prova = nome.upper()
dividido = prova.split()
print(f'Seu nome completo: {prova}| Primeiro nome: {dividido[0]}| Último nome: {dividido[-1]}|')
