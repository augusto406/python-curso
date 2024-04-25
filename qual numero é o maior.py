from time import sleep
n1 = float(input('qual o primeiro numero? '))
n2 = float(input('qual o segundo numero? '))
n3 = float(input('qual o terceiro numero? '))
if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('analisando...')
sleep(2)
print(f'o menor valor foi {menor:.0f} ')
print(f'o maior valor foi {maior:.0f} ')
