primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10-1)

for c in range (primeiro,decimo,razão):
    print('{}'.format(c), end=' - ')
print('ACABOU')
