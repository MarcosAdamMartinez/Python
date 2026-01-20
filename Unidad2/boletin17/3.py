import re

def comprobarCodigo():
    lista = list()
    contador_erroneos = 0
    contador_correctos = 0

    try:
        fichero = open("ficheros/codigos.txt", "r+")
        sigue = True

        while sigue:
            linea = fichero.readline()
            linea = linea.replace("\n", "")
            linea = linea.replace(" ", "")

            if re.match(r"^[A-Z]{2}[0-9]{22}$",linea):
                lista.append(linea)
                contador_correctos = contador_correctos + 1
            elif linea == "":
                sigue = False
            else:
                contador_erroneos = contador_erroneos + 1

        fichero.close()
    except:
        print("Error")

    for elemento in lista:
        print(f"Pais: {elemento[0:2]}\n"
              f"DC: {elemento[2:4]}\n"
              f"Entidad: {elemento[4:8]}\n"
              f"Sucursal: {elemento[8:12]}\n"
              f"DC cuenta: {elemento[12:14]}\n"
              f"Numero de cuenta: {elemento[14:24]}\n")
    print(f"Hay {contador_correctos} codigos correctos y {contador_erroneos} erroneos.")


comprobarCodigo()