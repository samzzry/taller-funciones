def pedir_cpu():
    c = float(input("Uso de CPU (%): "))
    return c

def procesar_cpu():
    alertas = 0
    mediciones = 0

    uso = pedir_cpu()

    while uso >= 0:
        mediciones = mediciones + 1

        if uso > 90:
            print("Alerta: Uso Crítico")
            alertas = alertas + 1

        uso = pedir_cpu()

    return alertas, mediciones

def mostrar_cpu(alertas, mediciones):
    print("Total de mediciones:", mediciones)
    print("Alertas críticas:", alertas)