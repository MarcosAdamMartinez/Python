import re

# Ejercicio 1: Valida si una cadena es un codigo postal Español
patron = r"^28[0-9]{3}"

if re.fullmatch(patron, "28530"):
    print("El codigo postal es valido")
else:
    print("El codigo postal no es valido")

# Ejercicio 2: Valida si una cadena es una matricula (4 nums seguidos de 3 letras mayusculas sin espacios)

patron = r"[0-9]{4}[A-Z]{3}"

if re.fullmatch(patron, "2341SAD"):
    print("La matricula es valida")
else:
    print("La matricula no es valida")

# Ejercicio 3: Valida si una cadena es una fecha
patron = r"(([0-2][0-9]|[0-3][0-1])/(0[1-9]|1[0-2])/[0-9]{4})|(([0-2][0-9]|[0-3][0-1])-(0[1-9]|1[0-2])-[0-9]{4})"

if re.fullmatch(patron, "01-02-2006"):
    print("La fecha es valida")
else:
    print("La fecha no es valida")

# Ejercicio 4: Valida si una cadena es un correo electronico

patron = r"(\w+)(.(\w+))*@(\w+).[a-z]{1,3}$"

if re.fullmatch(patron, "kevin.marcos@pene.pn"):
    print("El correo es valido")
else:
    print("El correo no es valido")

# Ejercicio 5: Valida si una cadena es un telefono con prefijo

patron = (r"^\+[0-9]{2}( )?[0-9]{9}$")

if re.fullmatch(patron, "+34 643660866"):
    print("El numero es valido")
else:
    print("El numero no es valido")

# Ejercicio 6: Valida si una cadena es una contraseña fuerte

patron = r"(?=.*[A-Z])(?=.*[0-9])[(A-Z)+a-z-0-9]{8,}"

# . implica cualquier caracter, * implica que puede existir o no ese caracter y que debe estar seguido por una mayuscula\
# si fuese .+ deberia haber un caracter antes de la mayuscula

if re.fullmatch(patron, "a3Aaaaaa"):
    print("La contraseña es valida")
else:
    print("La contraseña no es valida")


# Ejercicio 7: Valida si una cadena es un numer0 entero positivo o negativo

patron = (r"^-?[0-9]{1,}$")

if re.fullmatch(patron, "110"):
    print("El numero positivo o negativo es valido")
else:
    print("El numero positivo o negativo no es valido")


# Ejercicio 8: Valida si una cadena es una hora en formato de 24h

patron = (r"^([0-1][0-9]|2[0-3]):[0-5][0-9]$")

if re.fullmatch(patron, "23:39"):
    print("La hora es valida")
else:
    print("La hora no es valida")

# Ejercicio 9: Valida si una cadena es una tarjeta de credito

patron = (r"^[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4}$")

if re.fullmatch(patron, "1111 2222 3333 4444"):
    print("La tarjeta es valida")
else:
    print("La tarjeta no es valida")

# Ejercicio 10: Valida si una cadena es un nombre de usuario

patron = (r"^[A-Za-z-0-9-_]{3,15}$")

if re.fullmatch(patron, "nigga_adiosBro"):
    print("El nombre de usuario es valido")
else:
    print("El nombre de usuario no es valido")