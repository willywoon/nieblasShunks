from conection import Connection

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
            print('creacion de clientes: ')
            opt = int(input('1.- crear \n2.- modificar \n3.- eliminar \n4.- consultar' )) 

            if opt == 1:
                nuevaConexion.ingresarElemento()
            nuevaConexion.mostrarElemento()

        if op == 7:
            menu = False

menu()