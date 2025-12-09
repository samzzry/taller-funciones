def pedir_vendido():
    v = int(input("Cantidad vendida hoy: "))
    return v

def procesar_inventario():
    stock = 50
    punto = 10

    vendido = pedir_vendido()

    while vendido >= 0:
        stock = stock - vendido

        if stock <= punto:
            print("Aviso de Reposición Urgente")
            break

        vendido = pedir_vendido()

    return stock

def mostrar_inventario(stock):
    print("Stock final:", stock)