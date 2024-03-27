from math import factorial
from time import sleep

n = int(input('Digite o número para calcular o fatorial: '))
c = n
f = 1
print('Calculando {}!= '.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print('X'if c>1 else '=', end=' ')
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(n, f))
print('-=-'*10)
sleep(1)
print('Fim dos cálculos!!!')
print('-=-'*10)



