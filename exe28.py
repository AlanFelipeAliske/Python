import random
import time

"""
n1 = float (input('Digite a primeira nota: '))
n2 = float (input('Digite a segunda nota: '))

média = (n1 + n2) / 2

print(média)

if média >= 7.0:
    print('Você foi aprovado, Parabéns')
else: print('Você foi reprovado')
"""

numero_digitado = int(input('Digite um número de 0 a 5: '))
numero_aleatorio = random.randrange(0, 5)

print(' ** Processando... ** ')
time.sleep(2)

if numero_aleatorio == numero_digitado:
    print('Você acertou o número sorteado que foi {} ' .format(numero_digitado))
else:
    print('Você erro!! O número sorteado foi {} ' .format(numero_aleatorio))
