# if carro.esquerda():
#   bloco1
# elif carro.direita():
#   bloco2
# elif carro.ré():
#   bloco3
# else:
#   bloco4
# O 'if' pode ser utilizado apenas uma vez, o 'elif', quantas vezes você quiser, e o 'else', apenas uma vez.

nome = str(input('Qual seu nome? ')).strip().title()
if nome == 'Vini' or nome == 'Vinicius':
    print('Que nome top!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print(f'Seu nome é bem popular no Brasil, {nome}!')
else:
    print(f'Seu nome é bem normal, {nome}.')
print(f'Tenha um bom dia!')
