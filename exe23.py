
num = int(input('Digite um número de 0 a 9999: '))

print(num)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#print('Analisando um número: {} ' .format(n))

print('Unidae {} ' .format(u))
print('Dezena {} ' .format(d))
print('Centena {} ' .format(c))
print('Milhar {} ' .format(m))