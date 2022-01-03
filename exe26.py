frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase' .format(frase.count('A')))
print('A primeira letra "A" aparece na posição {} na frase' .format(frase.find('A')))
print('A ultima letra "A" aparece na posição {} na frase' .format(frase.rfind('A')))

