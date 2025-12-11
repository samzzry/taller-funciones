def pedir_codigo():
    codigo = input("ingrese su codigo de identificacion ")
    return codigo
def validar_codigo(codigo, codigo_especial):
    if codigo == codigo_especial:
        return True
    else:
        return False
def procesar_accesos():
    codigo_especial = "1234"
    permitidos = 0
    denegados = 0
    while True:
        cod = pedir_codigo()
        if cod == "salir":
            break
        if validar_codigo(cod, codigo_especial):
            print("accceso permitido")
            permitidos = permitidos + 1
        else:
            print("Acceso denegado.")
            denegados = denegados + 1
    return permitidos, denegados
def mostrar_resultados(permitidos, denegados):
    print("acceso permitido", permitidos)
    print("Acceso denegado", denegados)





// PROGRAMA PRINCIPAL
permitidos, denegados = procesar_accesos()
mostrar_resultados(permitidos, denegados)
