def pedir_venta():
    v = float(input("monto de venta del vendedor"))
    return v
def procesar_ventas():
    meta = 5000
    cumplidos = 0
    total = 0
    venta = pedir_venta()
    while venta > 0:
        total = total + 1
        if venta >= meta:
            cumplidos = cumplidos + 1
            print("meta cumplida")
        venta = pedir_venta()
    return cumplidos, total
def mostrar_ventas(cumplidos, total):
    print("vendedores con meta cumplida", cumplidos)
    print("total de vendedores procesados", total)

// programa principal
c, t = procesar_ventas()
mostrar_ventas(c, t)
