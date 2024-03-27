from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
opcao = 0
print('-=-' * 20)
while opcao != 5:
    print('''
    [1]Somar 
    [2]Multiplicar
    [3]Maior
    [4] Novos números 
    [5] Sair do Programa''')
    opcao = int(input('>>>>> Qual é a sua opção?: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} e {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os novos números: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção Inválida, Tente novamente!!')
print('-=-' * 20)
sleep(2)
print('Fim do Programa, Volte Sempre!!')
print('-=-' * 20)
