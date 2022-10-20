frase = str(input('Digite uma frase: ')).strip()
prova = frase.upper()
print(f'Quantas vezes aparece a letra "A"? {prova.count("A")}| Quando ela aparece pela primeira vez? {prova.find("A")}| E pela última? {prova.rfind("A")}')