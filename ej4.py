def pedir_unidades():
    u = int(input("Cantidad de unidades del lote: "))
    return u

def pedir_estado():
    e = input("Estado (D defectuosa / O ok): ")
    return e

def procesar_lotes():
    defectuosas = 0
    ok = 0

    seguir = input("Escriba STOP para terminar o ENTER para continuar: ")

    while seguir != "STOP":
        unidades = pedir_unidades()

        contador = 0
        while contador < unidades:
            estado = pedir_estado()

            if estado == "D":
                defectuosas = defectuosas + 1
            else:
                if estado == "O":
                    ok = ok + 1
                else:
                    print("Estado inválido")
                    contador = contador - 1

            contador = contador + 1

        seguir = input("Escriba STOP para terminar o ENTER para continuar: ")

    return defectuosas, ok

def mostrar_resumen(defectuosas, ok):
    total = defectuosas + ok

    if total > 0:
        porcentaje = (defectuosas * 100) / total
    else:
        porcentaje = 0

    print("Defectuosas:", defectuosas)
    print("OK:", ok)
    print("Porcentaje defectuosas:", porcentaje)