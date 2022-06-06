import os
from conection import Connection
from bancosShunks import Cuenta

def menuCliente(user):

    menu = True
    nuevaConexion = Connection()

    dinosaurio = nuevaConexion.mostrarCuentaCodigoUsuario(user[0])     #transformacion de datos en un objeto tipo cuenta
    nwUser = Cuenta(dinosaurio[0], dinosaurio[1], dinosaurio[2], dinosaurio[3], dinosaurio[4], user[1])
    
    while menu:

        print("""

        1.- Depositar en una cuenta.
        2.- Realizar un giro.
        3.- Consultar el saldo.
        4.- Mostrar el estado de la cuenta (desplegar todas las transacciones de una cuenta).
        5.- salir del menú.

        """)

        op = int(input('ingrese opcion: '))

        if op == 1:
            os.system('cls')
            print('Depositar a una cuenta')
            accion = 'deposito'
            id = input('ingrese id cuenta destino: ')

            monto = int(input('ingrese monto: '))
            
            if nwUser.girar(monto):
                nuevaConexion.modificarCuenta(nwUser.getCodigoCuenta(), nwUser.getSaldo()) # modificacion en la base de datos

                #-------------------------enviar dinero cuenta de destino
                destino = nuevaConexion.mostrarCuentaIdCuenta(id)
                cuentaDestino = Cuenta(destino[0], destino[1], destino[2], destino[3], destino[4])
                cuentaDestino.depositar(monto)
                nuevaConexion.modificarCuenta(id, cuentaDestino.getSaldo())

            #---------------------registro transaccion----------->
                nuevaConexion.ingresarTransaccion(nwUser.getCodigoCuenta(), id, monto, accion)
            
        if op == 2:
            os.system('cls')
            print('Realizar giro')
            monto = int(input('ingrese monto: '))
            nwUser.girar(monto)
            accion = 'giro'
            nuevaConexion.modificarCuenta(nwUser.getCodigoCuenta(), nwUser.getSaldo())

            #---------------------registro transaccion----------->
            nuevaConexion.ingresarTransaccion(nwUser.getCodigoCuenta(), 'giro', monto, accion)

        if op == 3:
            os.system('cls')
            print('Consultar saldo')
            print("Su saldo actual es: ", nwUser.getSaldo())

        if op == 4:
            os.system('cls')
            print('estado de cuenta')
            print('------------------------------>')
            nuevaConexion.verTrasaccion(nwUser.getCodigoCuenta())
            print('saldo actual: ', nwUser.getSaldo())

        if op == 5:
            os.system('cls')
            print("adios")
            nuevaConexion.cerrarConexion()
            menu = False
