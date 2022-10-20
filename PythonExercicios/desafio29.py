vel = int(input('Quantos KM/h você foi flagrado? '))
multa = (vel-80)*7
if vel <= 80:
    print(f'Sua velocidade de {vel}Km/h não agride nenhuma lei. Prossiga com a direção defensiva.')
else:
    print(f'Sua velocidade de {vel}Km/h agrediu a lei (limite de 80km/h)! Multa: R${multa:.2f}')
print('Sempre dirija com segurança.')