tot18 = totM = totM20 =0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18+=1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade <20:
        totM20 +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas maiores de 18 = {tot18}')
print(f'Total de homens cadastrados : {totM}')
print(f'Total de Mulheres com menos de 20 : {totM20}')
print('Fim')


