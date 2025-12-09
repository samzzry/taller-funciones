def pedir_producto():
    p = int(input("¿Qué producto lleva? "))
    return p

def cantidad_producto():
    pedidos = int(input("Digite la cantidad de pedidos: "))
    return pedidos

def procesar_datos(pedidos):
    suma = 0
    contador = 0
    
    for i in range(pedidos):
        calificacion = int(input(f"Del 1 al 5, ¿qué calificación le da al pedido {i+1}? "))
        
        if calificacion > 5:
            calificacion = 5
        elif calificacion < 1:
            calificacion = 1
            
        if calificacion == 5:
            print("Excelente")
        
        suma += calificacion
        contador += 1
    
    return suma, contador

def hacer_calculo(suma, contador):
    if contador > 0:
        promedio = suma / contador
    else:
        promedio = 0
    return promedio

def mostrar_mensaje(promedio):
    print(f"El promedio de calificaciones es: {promedio:.2f}")
