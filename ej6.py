def pedir_cpu():
    c = float(input("uso de cpu "))
    return c
def procesar_cpu():
    alertas = 0
    mediciones = 0
    uso = pedir_cpu()
    while uso >= 0:
        mediciones = mediciones + 1
        if uso > 90:
            print("alerta uso critico")
            alertas = alertas + 1
        uso = pedir_cpu()
    return alertas, mediciones

def mostrar_cpu(alertas, mediciones):
    print("total de medicione", mediciones)
    print("alerta critica", alertas)


// programa principal
a, m = procesar_cpu()
mostrar_cpu(a, m)
