print("********************************")
print("bem-vindo ao jogo de adivinhação".upper())
print("********************************")

numero_secreto = 45
total_tentativas = 3
rodada = 1

for i in range(1, total_tentativas + 1):
    print("=================================")
    print("tentativa {} de {}".upper().format(rodada, total_tentativas))
    print("=================================")
    chute_usuario = int(input("Qual o numero secreto(1 e 100)? "))

    if chute_usuario < 1 or chute_usuario > 100:
        print("Sao validos apenas numeros entre 1 e 100")
        continue

    e_igual = chute_usuario == numero_secreto
    e_maior = chute_usuario > numero_secreto
    e_menor = chute_usuario < numero_secreto

    if e_igual:
        print("Parabéns voce acertou!")
        break
    elif e_maior:
        print("Que pena voce errou :(. O numero secreto é menor")
    elif e_menor:
        print("Que pena voce errou :(. O numero secreto é maior")

    rodada += 1

print("Fim de jogo")


