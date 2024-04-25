salario = float(input('qual o seu salario atual? '))
if salario >= 1250.00:
    salarionovo = salario + (salario * 10 / 100)
    print(f'o seu salario passou de {salario:.2f} reais para {salarionovo:.2f} reais!')
else:
    salario <= 1250.00
    salarionovo = salario + (salario * 15 / 100) 
    print(f'o seu salario passou de {salario:.2f} reais para {salarionovo:.2f} reais! ')
