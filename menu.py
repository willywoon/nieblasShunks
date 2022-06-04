from conection import Connection
from bancosShunks import Cuenta

def menuCliente(user):

    menu = True
    nuevaConexion = Connection()

    print(user[0])
    dinosaurio = nuevaConexion.mostrarCuentaCodigoUsuario(user[0])
    print(dinosaurio)

    nwUser = Cuenta(dinosaurio[0], dinosaurio[1], dinosaurio[2], dinosaurio[3], dinosaurio[4], user[1])
    


    while menu:

        #        1.- Crear Cuentas 

        print("""

        1.- Depositar en una cuenta.
        2.- Realizar un giro.
        3.- Consultar el saldo.
        4.- Mostrar el estado de la cuenta (desplegar todas las transacciones de una cuenta).
        5.- salir del menú.

        """)

        op = int(input('ingrese opcion: '))

        if op == 1:
            print('Depositar a una cuenta')

            id = input('ingrese id cuenta destino: ')

            monto = int(input('ingrese monto: '))
            
            if nwUser.girar(monto):
                nuevaConexion.modificarCuenta(nwUser.getCodigoCuenta(), nwUser.getSaldo()) # modificacion en la base de datos

                #enviar dinero cuenta de destino
                destino = nuevaConexion.mostrarCuentaIdCuenta(id)
                cuentaDestino = Cuenta(destino[0], destino[1], destino[2], destino[3], destino[4])
                cuentaDestino.depositar(monto)
                nuevaConexion.modificarCuenta(id, cuentaDestino.getSaldo())
            
        if op == 2:
            print('Realizar giro')
            monto = int(input('ingrese monto: '))
            nwUser.girar(monto)
            nuevaConexion.modificarCuenta(nwUser.getCodigoCuenta(), nwUser.getSaldo())

        if op == 3:
            print('Consultar saldo')
            print("Su saldo actual es: ", nwUser.getSaldo())

        if op == 4:
            print('estado de cuenta')
            print('todas las transacciones y estado de cuenta')

        if op == 5:
            print("adios")
            nuevaConexion.cerrarConexion()
            menu = False

def menuAdministrador():

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
            print('Crear cuenta de usuarios (adm o cliente)')
            a = input("ingrese codigo usuario: ")
            b = input("ingrese nombre cliente: ")
            c = input("ingrese nombre usuario (para loguiar): ")
            d = input("ingrese password usuario (contraseña para loguaer): ")
            e = input("ingrese  estado usuario: ")
            f = input("ingrese tipo usuario (adm o cliente): ")

            nuevaConexion.ingresarUsuario(a, b, c, d, e, f)

            if f == 'cliente':

                print("creacion cliente default con nombre y codigo de usuario")
                idCuenta = input('ingrese id cuenta: ')
                nuevaCuenta = Cuenta(codigoCuenta = idCuenta, nombre = b, codigoUsuario = a)
                nuevaConexion.ingresarCuenta(nuevaCuenta.getCodigoCuenta(), nuevaCuenta.getTipoCuenta(), nuevaCuenta.getSaldo(), nuevaCuenta.getCodigoCliente(), nuevaCuenta.getEstado())

        if op == 2:

            print('CRUD de cliente: ')

            opt = int(input('1.- crear \n2.- modificar \n3.- eliminar \n4.- consultar:\n' ))
             
            if opt == 1:
                print('ingrese datos de la cuenta')
                a = input("ingrese id cuenta: ")
                b = input("ingrese codigo usuario (ya debe existir!) ")

                nuevaCuenta = Cuenta(codigoCuenta = a, codigoUsuario = b)
                nuevaConexion.ingresarCuenta(nuevaCuenta.getCodigoCuenta(), nuevaCuenta.getTipoCuenta(), nuevaCuenta.getSaldo(), nuevaCuenta.getCodigoCliente(), nuevaCuenta.getEstado())
            
            if opt == 2:
                print('Modificar cliente (solo estado [0 , 1, 2, 99])')
                id = input('ingrese codigo cuenta: ')
                estado = int(input('ingrese nuevo estado: '))
                nuevaConexion.modificarCuentaEstado(id, estado)
            
            if opt == 3:
                print('Eliminar cuenta')
                id = input('ingrese id de cuenta a borrar: ')
                nuevaConexion.borrarCuenta()

            if opt == 4:
                print('consulta de cliente')
                id = input('ingrese id: ')
                resultado = nuevaConexion.mostrarCuentaIdCuenta(id)
                if resultado == None:
                    print('id usuario no existe:')
                else:
                    print('id cuenta es: {}, y su saldo es: {}'.format(resultado[0], resultado[2]))
        if op == 3:
            print("adios")
            nuevaConexion.cerrarConexion()
            menu = False

