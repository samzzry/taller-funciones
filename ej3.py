def pedir():
 t = input("Tipo D deposito R retiro o FIN: ")
    return t
def monto():
    m = float(input("mont "))
    return m
def procesar():
    saldo = 1000
    trans = 0
    tipo = pedir()
    while tipo != "FIN":
        if tipo == "D":
            m = monto()
            saldo = saldo + m
            trans = trans + 1
        else:
            if tipo == "R":
                m = monto()
                if saldo - m >= 0:
                    saldo = saldo - m
                    trans = trans + 1
                else:
                    print("no se puede retirar, saldo insuficiente")
            else:
                print("tipo no valido")

        tipo = pedir()
    return saldo, trans
def mostrar(saldo, trans):
    print("saldo final:", saldo)
    print("transacciones validas:", trans)

// PROGRAMA PRINCIPAL
saldo, trans = procesar()
mostrar(saldo, trans)
