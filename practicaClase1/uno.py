frase = input("Introduce una frase: ")
letra = input("Letra a mantener: ")

if len(letra) == 1:
    print("Resultado: ",end="")
    for x in frase:
        if x == letra:
            print(x,end="")
        elif x == " ":
            print(" ", end="")
        else:
            print("*", end="")