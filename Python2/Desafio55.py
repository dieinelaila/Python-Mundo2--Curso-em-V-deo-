maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {} pessoa : '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
             menor = peso

print('O MAIOR peso foi de {}Kg'.format(maior))
print('O MENOR peso foi de {}Kg'.format(menor))

