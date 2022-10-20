cidade = str(input('Digite o nome da sua cidade: ')).upper().strip()
dividido = cidade.split()
print(f'Nome da sua cidade: {cidade}| Começa com Santo? {"SANTO" in dividido[0]}')
