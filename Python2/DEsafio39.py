from  datetime import date
atual = date.today().year
nasc = int (input('ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade ==18:
    print('Você deve se alistar')

elif idade <18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos')
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
ano = atual + saldo
print('Seu alistamento será em {} anos'. format(ano))

elif not idade <= 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
ano = atual - saldo
print("Faltam {} anos para seu alistamento ". format(ano))


