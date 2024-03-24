from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Escolha : 
[0] PEDRA
[1] PAPEL 
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada?: '))
print('-=' * 20)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 20)
print('O Computador escolheu {}'.format(itens[computador]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('-=' * 20)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCE')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')
