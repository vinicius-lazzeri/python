import math
from math import sin, cos, tan
ang = float(input('Insire o angulo que deseja saber seno | cosseno | tangente: '))
ang1 = math.radians(ang)
print(f'Ângulo: {ang}| Seno: {math.sin(ang1):.2f}| Cosseno: {math.cos(ang1):.2f}| Tangente: {math.tan(ang1):.2f}|')
