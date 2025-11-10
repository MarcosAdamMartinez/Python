import re

patron = r"ola"

# Saber si empieza por algo:
if re.match(patron, "oladam2"):
    print("Hay coincidencia")
else:
    print("No hay coincidencia")


# Saber si existe en la cadena:
print()
if re.search(patron, "holadam2"):
    print("Se ha encontrado")
else:
    print("No se ha encontrado")


# Saber si hay coincidencia exacta:
print()
if re.fullmatch(patron, "ola"):
    print("Hay coincidencia exacta")
else:
    print("No hay coincidencia exacta")

# Coincidencias en rangos:
print()
if re.fullmatch(r"[0-9]{3,5}","12333"):
    print("Hay coincidencia en los nums")
else:
    print("No hay coincidencia en los nums")

print()
if re.fullmatch(r"[0-9]{8}[A-Za-zÑñ]","12333234A"):
    print("Hay coincidencia en el DNI")
else:
    print("No hay coincidencia en el DNI")


print()
if re.fullmatch(r"[1-9]|1[0-2]","12"):
    print("Hay coincidencia en el mes")
else:
    print("No hay coincidencia en el mes")


print()
if re.fullmatch(r"(\w+)","bananaboy448"):
    print("Hay coincidencia en el texto")
else:
    print("No hay coincidencia en el texto")


print()
if re.fullmatch(r"[0-9]?","7"):
    print("Hay coincidencia en el numero2")
else:
    print("No hay coincidencia en el numero2")


print()
if re.fullmatch(r"[^5]","6"):
    print("Hay coincidencia en el numero3 o letra")
else:
    print("No hay coincidencia en el numero3 o letra")