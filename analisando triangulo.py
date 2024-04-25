print('-=-' * 20)
print('analisador de triangulos')
print('-=-' * 20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 or r3 < r1 + r2:
    print('esses segmentos podem montar um triangulo!')
else:
    print('esses segmentos não formam um triangulo!')
