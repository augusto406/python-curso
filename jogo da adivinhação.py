from random import randint
from time import sleep
print('-=-' * 20)
print('irei pensar em numero de 0 a 5, tente adivinhar! ')
print('-=-' * 20)
computador = randint(0 , 5)
eu = int(input('qual numero vc acha que é? '))
print('PROCESSANDO......')
sleep(2)
print(f'eu pensei no numero {computador}')
if eu == computador:
    print('vc ganhou!')
else:
    print('eu ganhei! hahaha, tente novamente')
