from conection import Connection
from bancosShunks import Cliente

def menu():

    menu = True
    nuevaConexion = Connection()

    while menu:

        print("""

        1.- Crear Cuentas 
        2.- Crear (modificar, eliminar, consultar) Cliente
        3.- Depositar en una cuenta
        4.- Realizar un giro
        5.- Consultar el saldo de una cuenta por cliente.-
        6.- Mostrar el estado de la cuenta (desplegar todas las transacciones de una cuenta).
        7.- salir del menú

        """)

        op = int(input('ingrese opcion: '))

        if op == 1:
            nuevaConexion.ingresarElemento()

        if op == 2:
            print('CRUD de cliente: ')
            opt = int(input('1.- crear \n2.- modificar \n3.- eliminar \n4.- consultar:\n' ))
             
            if opt == 1:
                nwCliente = Cliente()
                nuevaConexion.ingresarCliente(nwCliente.getCodigoCuenta(), nwCliente.getTipoCuenta(), nwCliente.getSaldo(), nwCliente.getCodigoCliente(), nwCliente.getIdUsuario(), nwCliente.getEstado())

            if opt == 4:
                print('consulta de cliente')
                id = input('ingrese id')
                print(nuevaConexion.mostrarCliente(id))
                

        if op == 7:
            print("adios")
            menu = False

def menu2():
    pass


menu()