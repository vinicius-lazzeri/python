import math
a = int(input('Insire a altura do triângulo: '))
b = int(input('Insire a base do triângulo: '))
x = math.sqrt(a**2 + b**2)
print(f'Lado A: {a} |Lado B: {b}| Hipotenusa: {math.floor(x)}')
