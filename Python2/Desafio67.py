while True:
        n = int(input('Gostaria da Tabuada de qual Valor?: '))
        if n < 0:
            break

        for c in range(1, 11):
            print(f'{n}x{c}={n * c}')
        print('-=-' * 10)
print('Programa Finalizado! Obrigado')

