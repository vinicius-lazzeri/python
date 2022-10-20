from time import sleep
vprod = float(input('Insire o valor do produto: R$'))
metodo = int(input(f""" {' Digite a operação a ser utilizada ':=^40}
[ 1 ]: À vista em dinheiro/cheque      
[ 2 ]: À vista no cartão
[ 3 ]: Parcelado 2x no cartão
[ 4 ]: Parcelado 3x ou mais no cartão
Método de compra: """))
print(f' {" Processando compra... ":=^40} ')
sleep(3.5)
if metodo == 1:
    print(f'Valor do produto: R${vprod:.2f} | Valor final com 10% de desc: R${vprod-(vprod*(10/100)):.2f}')
elif metodo == 2:
    print(f'Valor do produto: R${vprod:.2f} | Valor final com 5% de desc: R${vprod-(vprod*(5/100)):.2f}')
elif metodo == 3:
    print(f'Valor do produto: R${vprod:.2f} | Valor final não sofrerá alterações.')
    print(f'Serão 2 parcelas de: R${vprod/2:.2f}')
elif metodo == 4:
    print(f'Valor do produto: R${vprod:.2f} | Valor final com acréscimo de 20%: R${vprod+(vprod*(20/100)):.2f}')
    print(f'Serão 3 parcelas de: R${(vprod+(vprod*(20/100)))/3:.2f}')
else:
    print('Operação inválida, execute o programa outra vez de maneira adequada.')
print('-=- Fim do Programa -=-')