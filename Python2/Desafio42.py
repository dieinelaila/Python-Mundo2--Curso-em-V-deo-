
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:

    print('Os segmentos podem formar um triângulo', end=' ')

    if r1 == r2 == r3:
        # Triângulo equilátero
        print('Equilátero')

    elif r1 != r2 != r3 != r1:
        # Triângulo escaleno
        print('Escaleno')

    else:
        # Triângulo isósceles
        print('Isósceles')

else:
    # Se não, informar que os segmentos não formam um triângulo
    print('Os segmentos não podem formar triângulos')
