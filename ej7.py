def pedir_venta():
    v = float(input("Monto de venta del vendedor: "))
    return v

def procesar_ventas():
    meta = 5000
    cumplidos = 0
    total_vendedores = 0

    venta = pedir_venta()

    while venta > 0:
        total_vendedores = total_vendedores + 1

        if venta >= meta:
            cumplidos = cumplidos + 1
            print("Meta cumplida")

        venta = pedir_venta()

    return cumplidos, total_vendedores

def mostrar_ventas(cumplidos, total_vendedores):
    print("Vendedores con meta cumplida:", cumplidos)
    print("Total de vendedores procesados:", total_vendedores)