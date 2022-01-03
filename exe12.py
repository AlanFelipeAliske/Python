import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

hi = math.hypot(co, ca)

print('Medida do cateto oposto {}, medida do cateto adjacente {}, medida da hipotenusa {:.2f}' .format(co, ca, hi))