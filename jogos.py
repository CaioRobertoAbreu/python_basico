import adivinhacao_com_numeros_aleatorios
import forca

print("********************************")
print("bem-vindo ao Python jogos".upper())
print("********************************")

print("(1) Adivinhação")
print("(2) Forca")
jogo = int(input("Qual voce quer jogar? "))

if jogo == 1:
    adivinhacao_com_numeros_aleatorios.jogar()
elif jogo == 2:
    forca.jogar()

