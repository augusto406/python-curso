#menu
print('''\033[0;40;33m[1] calcular \n [2] exit\033[m''')
resposta = float(input('o que você deseja fazer?: '))
if resposta == 1:
    print('[1] adição \n [2] subtração \n [3] multiplicação \n [4] divisão ')
    op = float(input('qual calculo deseja fazer: '))
else:
    exit()
if op == 1:
    x = float(input('digite o primeiro valor: ')) #soma
    y = float(input('digite o segundo valor: '))
    soma = x + y
    print(soma)

elif op == 2:
    x = float(input('digite o primeiro valor: ')) #subtração
    y = float(input('digite o segundo valor: '))
    sub = x - y 
    print(sub)

elif op == 3:
    x = float(input('digite o primeiro valor: ')) #multiplicação
    y = float(input('digite o segundo valor: '))
    mult = x * y
    print(mult)

elif op == 4:
    x = float(input('digite o primeiro valor: ')) #divisão
    y = float(input('digite o segundo valor: '))
    div = x % y
    print(div)
