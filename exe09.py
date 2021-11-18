import math
import random
"""
valor = float(input('Digite o valor do produto: '))

res = valor - ((valor * 5) / 100)

print('O valor do produto e R${} com desconto vai fica R${} \n' .format(valor, res))

----------------------------------------------------------------------

salario = int(input('Digite o seu salrio: '))

reajuste = salario + (salario * 15 / 100)

print('Seu novo salario sera de {}' .format(reajuste))
"""

diasRodados = float(input('Digite quantos dias voce ficou com o carro: '))

km = float(input('Digite quantos Quilometros voce rodou: '))

res = (diasRodados * 60) + (km * 0.15)

print('Valor a pagar R${:.2f}' .format(res))