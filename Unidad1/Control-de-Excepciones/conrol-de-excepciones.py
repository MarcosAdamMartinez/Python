print("Inicio del programa")
try:
    denominador = int(input("Introduce el denominador: "))
    x = 45/denominador
    print(x)
except ValueError:
    print("Excepcion, introduce numeros, no letras")
except ZeroDivisionError:
    print("Excepcion, no se puede dividir entre 0")
except:
    print("Excepcion no reconocida")
else:
    print("No ha ocurrido ninguna excepcion")
finally:
    print("Haya o no haya excepcion")

print("Fin del programa")