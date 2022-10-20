from time import sleep
casa = float(input('Qual valor da casa a ser comprada? R$'))
print('Próxima pergunta...')
sleep(2)
salario = float(input('Qual seu salário atual? R$'))
print('Próxima pergunta...')
sleep(2)
anos = float(input('Em quantos anos você pretende quitar a casa? '))
print('Analisando! Isso pode levar alguns minutos...')
sleep(6)
print('---Teste - Fim do programa---')
pmensal = casa/(anos*12)
if pmensal > (salario*(30/100)):
    print(f'A prestação custará R${pmensal:.2f}, maior que seu aporte (R${salario:.2f}) necessário para o empréstimo.')
    print('Você precisa analisar uma propriedade mais barata. Volte sempre!')
else:
    print(f'A prestação custará R${pmensal:.2f}. Parabéns! Análise de empréstimo para as prestações foi APROVADA!')
    print('Pode prosseguir com o processo para a compra de uma casa!')
print('----- FIM DE ANÁLISE -----')
