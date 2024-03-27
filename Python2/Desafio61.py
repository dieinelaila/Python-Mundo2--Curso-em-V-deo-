from time import sleep

print('-=-' * 20)
print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA : '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{}'.format(termo), end=' ')
    termo += razão
    cont += 1

sleep(1)
print('-=-' * 20)
print('Fim da Contagem !!!')



