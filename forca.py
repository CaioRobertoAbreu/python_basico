def jogar():
    imprime_titulo()

    palavra_secreta = define_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    enforcou = False
    acertou = False
    tentativas = 1

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = pede_chute()

        if chute in palavra_secreta:
            verifica_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            tentativas += 1

        enforcou = tentativas == 8
        acertou = "_" not in letras_acertadas
        imprime_letras_acertadas(letras_acertadas)

    if acertou:
        print(f"\nParabens voce ganhou! Fim de jogo. Palavra: {palavra_secreta}")
    else:
        print(f"Que pena nao foi dessa vez :(. Fim de jogo. Palavra: {palavra_secreta}")


def imprime_titulo():
    print("********************************")
    print("bem-vindo ao jogo da forca".upper())
    print("********************************")


def imprime_letras_acertadas(letras_acertadas):
    print(f"Palavra Secreta: {letras_acertadas}")


def define_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    lista_palavras = {linha.strip() for linha in arquivo}
    arquivo.close()

    for palavra in lista_palavras:
        return str(palavra).lower()


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input(f"Infome uma letra: ")
    return chute.strip().lower()


def verifica_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = chute.upper()
        index += 1


if __name__ == "__main__":
    jogar()
