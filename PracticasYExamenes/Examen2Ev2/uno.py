def esconderPin(numero : int) -> tuple:
    numeroLista = list(str(numero))
    palabrasCifradas = list()
    for c in numeroLista:
        if not c.isdigit():
            return "Parametro pasado no es un pin"
    while len(numeroLista) < 4:
        numeroLista.insert(0,0)
    for c in numeroLista:
        if int(c) == 0:
            elemento = f"{int(c):X>10}"
        elif int(c) == 1:
            elemento = "0XXXXXXXXX"
        elif int(c) == 2:
            elemento = "X0XXXXXXXX"
        elif int(c) == 3:
            elemento = "XX0XXXXXXX"
        elif int(c) == 4:
            elemento = "XXX0XXXXXX"
        elif int(c) == 5:
            elemento = "XXXX0XXXXX"
        elif int(c) == 6:
            elemento = "XXXXX0XXXX"
        elif int(c) == 7:
            elemento = "XXXXXX0XXX"
        elif int(c) == 8:
            elemento = "XXXXXXX0XX"
        elif int(c) == 9:
            elemento = "XXXXXXXX0X"
        palabrasCifradas.append(elemento)
    tupla = tuple(palabrasCifradas)
    return tupla

numero = 6240
for elemento in esconderPin(numero):
    print(elemento)
