distancia = int(input('quantos km é a sua viagem? '))
if distancia <= 200:
    preço=int(0.50 * distancia)
    print(f'o preço da sua viagem será de {preço} reais! ')
else:
    preço=int(0.45 * distancia)
    print(f'o preço da sua viagem será de {preço} reais! ')
    