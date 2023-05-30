def mostra():
    #   LIST COMPREHENSION
    inteiros = [n for n in range(1, 35)]
    print(inteiros)
    pares = [p for p in inteiros
             if p % 2 == 0]
    print(pares)


if __name__ == "__main__":
    mostra()
