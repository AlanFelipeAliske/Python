velocidade = int (input('Digite a velocidade: '))

if velocidade > 80:
    multa = float (velocidade - 80) * 7
    print('Você foi multado por estar acima de 80 KMH')
    print('O valor da sua multa é R$ {:.2f} ' .format(multa))

else: print('Sua velocidade atual é {} KM ' .format(velocidade))