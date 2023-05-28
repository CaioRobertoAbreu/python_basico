import random


def jogar():
    print("********************************")
    print("bem-vindo ao jogo de adivinhação".upper())
    print("********************************")

    numero_secreto = random.randrange(1, 101)

    print("Niveis: [1] Facil - [2] Medio - [3] Dificil")
    nivel = int(input("Escolha seu nível: "))

    pontos = 1000
    total_tentativas = 0
    if nivel == 1:
        total_tentativas = 9

    elif nivel == 2:
        total_tentativas = 6

    elif nivel == 3:
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
            print(f"Parabéns voce acertou! Pontos: {pontos}")
            break
        elif e_maior:
            print("Que pena voce errou :(. O numero secreto é menor")
        elif e_menor:
            print("Que pena voce errou :(. O numero secreto é maior")

        pontos_perdidos = abs(numero_secreto - chute_usuario)
        pontos = pontos - pontos_perdidos
        # print(f"Pontos Perdidos: {pontos_perdidos}")
        rodada += 1

    print("Fim de jogo")
    print(f"Numero aleatorio: {numero_secreto}")

if __name__ == "__main__":
    jogar()
