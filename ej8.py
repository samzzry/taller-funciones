def pedir_edad():
    e = int(input("Edad del participante: "))
    return e

def procesar_edades():
    publico = 0
    suma_edades = 0
    total_personas = 0

    edad = pedir_edad()

    while edad != 0:
        total_personas = total_personas + 1
        suma_edades = suma_edades + edad

        if edad >= 25 and edad <= 45:
            publico = publico + 1
            print("Registrado dentro del público objetivo")

        edad = pedir_edad()

    return publico, suma_edades, total_personas

def mostrar_edades(publico, suma_edades, total_personas):
    if total_personas > 0:
        promedio = suma_edades / total_personas
    else:
        promedio = 0

    print("Público objetivo:", publico)
    print("Promedio de edad:", promedio)