sexo = str(input('Informe seu Sexo: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos!, Informe seu Sexo :')).strip().upper()[0]
print('Sexo {} registrado com sucesso '.format(sexo))





