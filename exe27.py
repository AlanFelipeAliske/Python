"""
import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


for number in range(6):
    number = random.randrange(0, 61)
    print(number)

"""

nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()

print('Muito prazer {} esse é seu primeiro nome, e o ultimo nome é: {} ' .format(nome_separado[0], nome_separado[len(nome_separado)-1]))




