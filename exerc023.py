import random
#https://wiki.python.org.br/ManipulandoStringsComPython
num = int(random.randint(0,9999))
n = str(num)

u = num//1 %10
d = num//10 %10
c = num//100 %10
m = num//1000 %10

print('----'*20)
print('Analisando o número: {}'.format(num))
print('Unidade : {}'.format(u))
print('Dezena : {}'.format(d))
print('Centena : {}'.format(c))
print('Milhar : {}'.format(m))

print('----'*20)


