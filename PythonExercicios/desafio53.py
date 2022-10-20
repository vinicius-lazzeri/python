# Desafio 53 Criar um PALINDROMO "Apos a sopa" | "A SACADA DA CASA"
frase = str(input('Cite uma frase qualquer: ')).upper().strip()
junta = frase.replace(" ", "")
frase2 = junta[::-1]
if junta == frase2:
    print(f'A frase "{frase}" é um palindromo! ')
else:
    print(f'A frase "{frase}" NÃO é um palindromo! ')