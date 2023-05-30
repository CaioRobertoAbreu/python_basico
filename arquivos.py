def escrita():
    print("ESCRITA DE ARQUIVOS")
    arquivo = open("palavras.txt", "w")
    arquivo.write("Maca\n")
    arquivo.write("Melancia\n")
    arquivo.write("Pessego\n")
    arquivo.close()


# O escrita vai sobreescrever
def adiciona_no_arquivo():
    print("Adicionando ao arquivo".upper())
    arquivo = open("palavras.txt", "a")
    arquivo.write(input("Informa uma palavra: ").lower())
    arquivo.close()


def leitura():
    print("leitura de arquivos".upper())
    arquivo = open("palavras.txt", "r")
    arquivo_lido = arquivo.readline()
    print(arquivo_lido)
    arquivo.close()


if __name__ == "__main__":
    leitura()
