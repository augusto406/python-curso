from random import randint
from time import sleep

print('-=-' * 20)  #menu do jogo
print('''\033[1;35;40mmenu do jogo
[1] - START THE GAME!
[2] - EXIT\033[m''')
print('-=-' * 20)

print('\033[37;40m=\033[m' * 20)
decisao = str(input('\033[1;32;40mchoice!\033[m')) #sub menu
print('=' * 20)

print('-=-' * 20)  #jogadas
if decisao == '1':
    print('''\033[1;33;40mJOGADAS
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA\033[m''')  

else:
    exit()
print('-=-' * 20)
itens =('pedra' , 'papel' , 'tesoura') 
computador = randint(0 , 2)

print('-=-' * 20)
jogador = int(input('\033[1;34;40mqual é sua jogada?\033[m')) #jogada do jogador 
print('-=-' * 20)
print('\033[1;36;40mJO\033[m')
sleep(1)
print('\033[1;36;40mKEN\033[m')
sleep(1)
print('\033[1;36;40mPÔ\033[m')
sleep(1)

print('=' * 20)
print(f'\033[1;32;40mcomputador jogou {itens[computador]}\033[m') #jogada do computador e do jogador 
print(f'\033[1;33;40mjogador jogou {itens[jogador]}\033[m')
print('=' * 20)

if computador == 0:            #sistema do jogo
    if jogador == 0:
        print('\033[30;42mEMPATE\033[m')
    elif jogador == 1:
        print('\033[1;32;40mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;34;40mCOMPUTADOR VENCE!\033[m')
    else:
        print('\033[1;31;40mJOGADA INVALIDA!\033[m')
if computador == 1:
    if jogador == 1:
        print('\033[30,42mEMPATE!\033[m')
    elif jogador == 0:
        print('\033[1;34;40mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;32;40JOGADOR VENCE!\033[m')
    else:
        print('\033[1;31;40mJOGADA INVALIDA!\033[m')
if computador == 2:
    if jogador == 2:
        print('\033[30;40mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;34;40mCOMPUTADOR VENCE!\033[m')
    elif jogador == 0:
        print('\033[1;32;40mJOGADOR VENCE!\033[m')
    else:
        print('\033[1;31;40mJOGADA INVALIDA!\033[m')
print('=' * 20)
