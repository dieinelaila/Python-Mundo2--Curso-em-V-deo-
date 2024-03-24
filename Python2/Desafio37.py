num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opçao=int (input('Sua opção: '))

if opçao ==1:
  print('{} Convertido para Binário é igual a {}'.format(num, bin(num)))

elif opçao ==2:
 print('{} Convertido para Octal é igual a {}'.format(num, oct(num)))

elif opçao ==3:
 print('{} Convertido para Hexadecimal é igual a {}'.format(num,hex(num)))

else:
 print('Opção inválida, Tente novamente')



