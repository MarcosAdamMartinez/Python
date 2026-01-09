def calcularMascara():
    ip = input("Introduce una direccion IP: ")
    numeros = ip.split(".")
    if len(numeros) != 4:
        return "Direccion no valida"
    else:
        cont = 0

        for num in numeros:
            cont += 1
            if num.isdigit():
                if 0 <= int(num) <= 256:
                    if cont == 4:
                        if int(num) == 0:
                            return "Direccion reservada"
                        elif int(num) in range(1,128):
                            return ip+"/8"
                        elif int(num) in range(128,192):
                            return ip+"/16"
                        elif int(num) in range(192,224):
                            return ip+"/32"
                        elif int(num) in range(224,256):
                            return "Direccion reservada"
                else:
                    return "Direccion no valida"
            else:
                return "Direccion no valida"

print(calcularMascara())
