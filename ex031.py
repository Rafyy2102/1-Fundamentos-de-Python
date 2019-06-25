distancia = float(input("Qual a distância da sua viagem? "))
print("Você está prestes a comecar uma viagem de {}Km.".format(distancia))
"""if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45"""
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print("É o preço de sua passagem será de R${:.2f}".format(preço))