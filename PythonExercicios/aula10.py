#aula 10 - condições
#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <=3:
#    print('carro novo')
#else:
#    print('carro velho')
#print('FIM')
#modo simplificado:
#tempo = int(input('Quantos anos tem seu carro? '))
#print('carro novo' if tempo<=3 else 'carro velho')
#print('FIM')

#nome = str(input('Qual seu nome? '))
#if nome == 'Vini':
#    print('Que nome lindo vc tem!')
#    print(f'Bom dia, {nome}!')
#else:
#    print(f'Porra! {nome} é um nome feio bagarai')
#print('Fim')#

#nome = str(input('Qual seu nome? ')) - Condição Simplificada
#if nome == 'Vini':
#    print(f'Que nome lindo você tem, {nome}!')
#print(f'Bom dia, {nome}!')

n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insire a segunda nota do aluno: '))
md = (n1+n2)/2
if md >= 7:
    print(f'Sua nota foi {md}, você foi aprovado, parabéns!')
else:
    print(f'Sua nota foi {md}, você foi reprovado, que vergonha!')
print('--- FIM ---')
