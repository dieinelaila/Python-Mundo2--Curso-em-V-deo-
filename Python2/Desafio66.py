soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print('-=-'*10)
print(f'A soma dos valores foi {soma}')
print(f'A quantidade de números digitados foi {cont}')
print('-=-'*10)


