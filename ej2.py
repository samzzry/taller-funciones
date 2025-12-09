def pedir_codigo():
    codigo = input("Ingrese su código de identificación: ")
    return codigo

def validar_codigo(codigo, codigo_especial):
    if codigo == codigo_especial:
        return True
    else:
        return False

def procesar_accesos():
    codigo_especial = "INV-001"
    permitidos = 0
    denegados = 0

    while True:
        cod = pedir_codigo()
        if cod.upper() == "SALIR":
            break

        if validar_codigo(cod, codigo_especial):
            print("Acceso permitido.")
            permitidos += 1
        else:
            print("Acceso denegado.")
            denegados += 1
    
    return permitidos, denegados

def mostrar_resultados(permitidos, denegados):
    print(f"Accesos permitidos: {permitidos}")
    print(f"Accesos denegados: {denegados}")