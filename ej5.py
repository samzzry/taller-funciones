def pedir_precio():
    p = float(input("Precio del producto: "))
    return p

def pedir_cantidad():
    c = int(input("Cantidad: "))
    return c

def procesar_compra():
    subtotal = 0
    seguir = input("¿Agregar producto? (S/N): ")

    while seguir != "N":
        precio = pedir_precio()
        cantidad = pedir_cantidad()

        subtotal = subtotal + (precio * cantidad)

        seguir = input("¿Agregar otro producto? (S/N): ")

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
    print("Descuento aplicado:", desc)
    print("Monto final a pagar:", total)