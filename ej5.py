def pedir_precio():
    p = float(input("precio del producto: "))
    return p
def pedir_cantidad():
    c = int(input("cantidad: "))
    return c
def procesar_compra():
    subtotal = 0
    seguir = input("agregar producto (si/no): ")
    while seguir != "no":
        precio = pedir_precio()
        cantidad = pedir_cantidad()
        subtotal = subtotal + (precio * cantidad)
        seguir = input("agregar otro producto (si/no): ")
    return subtotal
def calcular_descuento(subtotal):
    if subtotal > 1000:
        desc = subtotal * 0.10
    else:
        if subtotal > 500:
            desc = subtotal * 0.05
        else:
            desc = 0
    total = subtotal - desc
    return total, desc
def mostrar_total(total, desc):
    print("descuento aplicado:", desc)
    print("monto final a pagar:", total)
// programa principal
subtotal = procesar_compra()
total, desc = calcular_descuento(subtotal)
mostrar_total(total, desc)
