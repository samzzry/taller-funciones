def pedir_unidades():
    u = int(input("cantidad de unidades del lote "))
    return u
def pedir_estado():
    e = input("estado (D defectuosa / O ok) ")
    return e
def procesar():
    defectuosas = 0
    ok = 0
    seguir = input("Escriba stop para terminar o enter para continuar: ")

    while seguir != "stop":
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

        seguir = input("escriba  stop para terminar o ente para continuar: ")

    return defectuosas, ok

def mostrar(defectuosas, ok):
    total = defectuosas + ok

    if total > 0:
        porcentaje = (defectuosas * 100) / total
    else:
        porcentaje = 0

    print("defectuosa", defectuosas)
    print("ok:", ok)
    print("porcentaje defectuosa ", porcentaje)

// programa principal
d, o = procesar()
mostrar(d, o)
