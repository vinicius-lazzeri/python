from time import sleep
peso = float(input('Insire seu peso: '))
altura = float(input('Insire sua altura em metros: '))
imc = peso/(altura**2)
print('Analisando IMC...')
sleep(3.5)
if imc < 18.5:
    print(f'Seu IMC é de: {imc:.1f}, você está abaixo do peso!')
elif imc < 25:
    print(f'Seu IMC é de: {imc:.1f}, você está no peso ideal!')
elif imc < 30:
    print(f'Seu IMC é de: {imc:.1f}, você está em sobrepeso!')
elif imc < 40:
    print(f'Seu IMC é de: {imc:.1f}, você está obeso!')
else:
    print(f'Seu IMC é de: {imc:.1f}, você está com obesidade mórbida!')
print('Fim do programa')
