from conection import Connection
from bancosShunks import Cliente

def menuCliente():

    menu = True
    nuevaConexion = Connection()

    while menu:

        #        1.- Crear Cuentas 

        print("""

        1.- Depositar en una cuenta
        2.- Realizar un giro
        3.- Consultar el saldo de una cuenta por cliente.-
        4.- Mostrar el estado de la cuenta (desplegar todas las transacciones de una cuenta).
        5.- salir del menú

        """)

        op = int(input('ingrese opcion: '))


        if op == 1:
            print('Depositar a una cuenta')
            id = input('ingrese id cuenta destino: ')
            monto = input('ingrese monto: ')
            
            cli = nuevaConexion.mostrarCliente(id)
            cliente = Cliente(cli[0], cli[1], cli[2], cli[3], cli[4], cli[5])           #creacion de un objeto cliente con datos de la base de datos
            
            cliente.girar(monto)

            otroCliente = Cliente()
            otroCliente.depositar(monto)
        
        if op == 2:
            print('Realizar giro')
            monto = input('ingrese monto: ')

            cliente = Cliente()
            cliente.girar(monto)

        if op == 3:
            print('Consultar saldo')
            cliente = Cliente()
            cliente.consultarSaldo()

        if op == 4:
            print('estado de cuenta')
            print('todas las transacciones y estado de cuenta')

        if op == 5:
            print("adios")
            menu = False

def menu2():

    menu = True
    nuevaConexion = Connection()

    while menu:

        print("""

        1.- Crear Cuenta
        2.- Crear (modificar, eliminar, consultar) Cliente
        3.- salir del menú

        """)

        op = int(input('ingrese opcion: '))

        if op == 1:
            print('Crear cuenta: ')


        if op == 2:

            print('CRUD de cliente: ')

            opt = int(input('1.- crear \n2.- modificar \n3.- eliminar \n4.- consultar:\n' ))
             
            if opt == 1:
                nwCliente = Cliente()
                nuevaConexion.ingresarCliente(nwCliente.getCodigoCuenta(), nwCliente.getTipoCuenta(), nwCliente.getSaldo(), nwCliente.getCodigoCliente(), nwCliente.getIdUsuario(), nwCliente.getEstado())
            
            if opt == 2:
                print('Modificar cliente (solo estado)')
                id = input('ingrese codigo cuenta: ')
                nuevaConexion.modificarElemento(id)

            if opt == 4:
                print('consulta de cliente')
                id = input('ingrese id: ')
                cli = nuevaConexion.mostrarCliente(id)
                cliente = Cliente(cli[0], cli[1], cli[2], cli[3], cli[4], cli[5])
                print(cliente.getNombre())
        
        if op == 3:
            print("adios")
            menu = False


