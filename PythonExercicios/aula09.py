#frase = 'curso em video python' #21 indices
#fatiamento:
#frase[9] pega apenas a letra do índice | frase[9:13] faz do 9 até o 12|
#frase[9:21] vai até o ultimo, embora nao seja o ideal | frase[9:21:2] pula de 2 em 2
#frase[:5] vai do 0 ao 4| frase[15:] vai do 15 até o final| frase[9::3] 9 até o final pulando de 3
#Analise:
#len(frase) mensura o comprimento da frase|frase.count('o') pede para contar a palavra 'o'
#frase.count('o', 0, 13) conta 'o' do 0 ao 12| frase.find('deo') indica onde começa 'deo',q seria11
#frase.find('Android') qnd vc poe um valor inexistente, vai retornar -1 |
#'curso' in frase - retornaria True
#transformação:
#frase.replace('python', 'android') - procuraria 'python' e trocaria por 'android'
#frase.upper() - colocaria tudo em maiúsculo
#frase.lower() - colocaria tudo em minusculo
#frase.capitalize() - apenas o primeiro indice ficaria em maiúsculo
#frase.title() - as primeiras palavras apos espaço ficariam maiusculas: 'Curso Em Video'
#frase.strip() '   Aprenda Python   ' essa função removeria os espaços inuteis.
#frase.rstrip() - removeria apenas os ultimos espaços inuteis que estão no fim (direita)
#frase.lstrip() - removeria os espaços inuteis a esquerda, que estariam no começo
#divisão:
#frase.split() - divide a frase em seus espaços 'curso em video' > 'curso' 'em' 'video'
#gerando outra lista, cada uma dessas frases começando pelo indice 0
#junção:
#'-'.join(frase)- junta a frase. 'curso em video python' > 'curso-em-video-python'
frase = 'Curso em Video Python'
dividido = frase.split()
print(dividido[2][3])


