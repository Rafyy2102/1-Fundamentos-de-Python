from random import randint
from time import sleep
computador = randint(0, 5)#Faz o computador "PENSAR"
print("-=-" *20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" *20)
jogador = int(input("Em que número eu o pensei? "))#Jogador tenta adivinhar um número
print("PROCESSANDO...")
sleep(3)# Faz o computador pensar por uma breve parada
if jogador == computador:
    print("PARABENS! Você conseguiu vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}".format(computador, jogador))
