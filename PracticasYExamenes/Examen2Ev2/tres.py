import re

def validarMatricula(matricula):
    patron = r"[0-9]{4}(-| )[B-DF-HJ-PR-TV-Z]{3}"
    if re.fullmatch(patron, matricula):
        return True
    else:
        return False


def matriculasValidas(* matriculas):
    contadorCorrecto = 0
    contadorIncorrecto = 0

    for matricula in matriculas:
        if validarMatricula(matricula):
            print(matricula, "es valida")
            contadorCorrecto += 1
        else:
            print(matricula, "no es valida")
            contadorIncorrecto += 1

    print()
    print("Matriculas validas:",contadorCorrecto)
    print("Matriculas no validas:",contadorIncorrecto)


matriculasValidas("22CDR", "7521-MXP", "1224MN")
print()
matriculasValidas("5432 - BCF","3456BAC")