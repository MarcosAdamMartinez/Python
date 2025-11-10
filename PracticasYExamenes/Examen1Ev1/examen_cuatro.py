frac = input("Escribe tu fracción: ")
if frac.count("/") == 1:
    if frac.count(".") == 0:
        if not (frac.startswith("/") or frac.endswith("/")):
            frac = frac.replace(" ","")
            nums = frac.split("/")
            if nums[0].isdigit() and nums[1].isdigit():
                if not (int(nums[1]) == 0):
                    print("El valor de tu fracción es:",round(int(nums[0])/int(nums[1]),3))
                else:
                    print("Error, el segundo numero no puede ser 0")
            else:
                print("No se permiten letras en la fracción")
        else:
            print("La fracción no puede empezar o terminar por \"/\"")
    else:
        print("Ninguno de los 2 números puede ser decimal")
else:
    print("El numero debe estar separado por una unica \"/\"")