lar = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = lar * altura
print("Sua parede tem a dimensão de {} x {} e sua área é de {} m².".format(lar, altura, area))
tinta = area / 2
print("Para pintar essa parede, você precisará de {} litros de tinta.".format(tinta))