nome = str(input('Qual seu nome?:'))
if nome =='Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome=='Maria':
    print('Seu nome é popular no Brasil!')
elif nome in 'Dieine, sylvio, José':
    print('Seu nome é diferente no Brasil!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia {}!.'.format(nome))


