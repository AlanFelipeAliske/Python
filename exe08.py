n1 = float(input('Digite o altura da parede que deseja pintar: '))
n2 = float(input('Digite a largura da parede que deseja pintar: '))

tamanhoParede = n1 * n2

res = tamanhoParede / 2


print('Sua parede mede {} m²' .format(tamanhoParede))
print('Sao necessarias {} latas de tintas para pintar essa parede' .format(res))