print('{:^40}'.format(' Lojas Dieine '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista Dinheiro
[2] à vista Cartão 
[3] 2x Cartão 
[4] 3x ou mais Cartão''')
opçao = int(input('Qual é a opção?!: '))
if opçao == 1:
    total = preco - (preco * 10 / 100)
elif opçao == 2:
    total = preco - (preco * 5 / 100)
elif opçao ==3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2 x de R${:.2f} sem juros .'.format(parcela))
elif opçao ==4:
    total = preco + (preco *20/100)
    totpar = int(input('Quantas parcelas?'))
    parcela = total / totpar
    print('Sua compra será parcelada em {} vezes, e o valor será de R$ {:.2f} Com juros .'.format(totpar, parcela))
else:
    total = preco
    print('Opção Inválida, Tente novamente')
print('Sua compra de R$ {:.2f}, no final será de R${:.2f}'.format(preco, total))

