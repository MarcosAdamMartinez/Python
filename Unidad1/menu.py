opcion = input("P para jugar, C para configurar o X para salir\n")

match opcion:
    case "P" | "p" | "J" | "j":
        print("Has elegido jugar")
    case "C" | "c" :
        print("Has elegido Configurar")
    case "X" | "x":
        print("Has elegido Salir, hasta la proxima")
    case _:
        print("Opcion no valida")

print("Fin del menu")