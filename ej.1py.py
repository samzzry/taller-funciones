def pedir():
    p = int(input("que producto lleva "))
    return p
def cantidad():
    c = int(input("cuantos pedidos son "))
    return c
def procesar(c):
    total = 0
    cont = 0   
    for n in range(c):
        print("calificacion del pedido:")
        cal = int(input("Del 1 al 5 "))  
        if cal > 5:
            cal = 5
        if cal < 1:
            cal = 1
        if cal == 5:
            print("excelente")  
        total = total + cal
        cont = cont + 1
    return total, cont
def calcular(total, cont):
    if cont > 0:
        prom = total / cont
    else:
        prom = 0
    return prom
def mostrar(prom):
    print("El promedio es:", prom)
// PROGRAMA PRINCIPAL
producto = pedir()
cant = cantidad()
total, cont = procesar(cant)
prom = calcular(total, cont)
mostrar(prom)
