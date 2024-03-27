from time import sleep

print('-=-' * 20)
print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA : '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' ')
        termo += razão
        cont += 1
    print('CALCULANDO ')
    sleep(1)
    mais = int(input('Quantos termos você quer mostrar a mais?: '))
sleep(1)
print('-=-' * 20)
print('Fim da Contagem !!!')
