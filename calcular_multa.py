vel = int(input('qual a velocidade do carro? '))
if vel >= 80:
    print('vc foi multado!')
    multa=float(vel*7.00)
    print(f'vc foi multado em {multa:.0f} reais.')
else:
    print('vc estava na velocidade permitida!')