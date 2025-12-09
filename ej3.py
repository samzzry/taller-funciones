def pedir_tipo():
    t = input("Tipo (D depósito / R retiro / FIN): ")
    return t

def pedir_monto():
    m = float(input("Monto: "))
    return m

def procesar_transacciones():
    saldo = 1000
    transacciones = 0

    tipo = pedir_tipo()

    while tipo != "FIN":
        if tipo == "D":
            monto = pedir_monto()
            saldo = saldo + monto
            transacciones = transacciones + 1

        else:
            if tipo == "R":
                monto = pedir_monto()
                if saldo - monto >= 0:
                    saldo = saldo - monto
                    transacciones = transacciones + 1
                else:
                    print("No se puede retirar, saldo insuficiente")
            else:
                print("Tipo no válido")

        tipo = pedir_tipo()

    return saldo, transacciones

def mostrar_balance(saldo, transacciones):
    print("Saldo final:", saldo)
    print("Transacciones válidas:", transacciones)