def pedir_horas():
    h = int(input("Horas extra trabajadas: "))
    return h

def procesar_horas():
    total_bono = 0
    empleados_bono = 0

    horas = pedir_horas()

    while horas >= 0:
        if horas > 5:
            bono = horas * 15
            total_bono = total_bono + bono
            empleados_bono = empleados_bono + 1
        else:
            if horas > 0:
                bono = horas * 10
                total_bono = total_bono + bono
                empleados_bono = empleados_bono + 1

        horas = pedir_horas()

    return total_bono, empleados_bono

def mostrar_bonos(total_bono, empleados_bono):
    print("Bonificación total:", total_bono)
    print("Empleados con bonificación:", empleados_bono)