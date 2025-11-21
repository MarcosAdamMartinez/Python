def funcionBinario(binario):
    sumaDecimal = 0
    contador = 0
    cadena = binario[::-1]
    for numero in cadena:
        if numero.isdigit():
            if int(numero) == 1:
                sumaDecimal += 2 ** contador
            elif int(numero) == 0:
                sumaDecimal += 0
            else:
                sumaDecimal = -1
            contador += 1
        else:
            sumaDecimal = -1

    return sumaDecimal

def funcionBinario2(binario):
    decimal = 0
    try:
        decimal = int(binario, 2)
    except ValueError:
        decimal = -1
    return decimal

print(funcionBinario("10110"))
print(funcionBinario2("10110"))
print(funcionBinario("345"))
print(funcionBinario2("345"))
print(funcionBinario("hola"))
print(funcionBinario2("hola"))
