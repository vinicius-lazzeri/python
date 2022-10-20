a = float(input('lado A: '))
b = float(input('lado B: '))
c = float(input('lado C: '))
if a < b+c and b < a+c and c < b+a:
    print('Sim! Um triângulo poderá ser formado com essas 3 retas.')
    if a == b == c:
        print('Este triângulo será EQUILÁTERO')
    if a != b or a != c or b != c:
        print('Este triângulo será ESCALENO')
    else:
        print('Este triângulo será ISÓSCELES')
else:
    print('Não! Um triângulo não poderá se formar com essas 3 retas.')
print('---FIM---')


