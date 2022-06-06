import os
from conection import Connection
from bancosShunks import Cuenta
from login import cifrar

def menuAdm():

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

            passCifrada = cifrar(d, 'md5')

            nuevaConexion.ingresarUsuario(a, b, c, passCifrada, e, f)

            if f == 'cliente':

                print("creacion cliente default con nombre y codigo de usuario")
                idCuenta = input('ingrese id cuenta: ')
                nuevaCuenta = Cuenta(codigoCuenta = idCuenta, nombre = b, codigoUsuario = a)
                nuevaConexion.ingresarCuenta(nuevaCuenta.getCodigoCuenta(), nuevaCuenta.getTipoCuenta(), nuevaCuenta.getSaldo(), nuevaCuenta.getCodigoCliente(), nuevaCuenta.getEstado())

        if op == 2:
            os.system('cls')
            print('CRUD de cliente: ')
            opt = int(input('1.- crear \n2.- modificar \n3.- eliminar \n4.- consultar:\n' ))
             
            if opt == 1:
                os.system('cls')
                print('ingrese datos de la cuenta')
                a = input("ingrese id cuenta: ")
                b = input("ingrese codigo usuario (ya debe existir!) ")

                nuevaCuenta = Cuenta(codigoCuenta = a, codigoUsuario = b)
                nuevaConexion.ingresarCuenta(nuevaCuenta.getCodigoCuenta(), nuevaCuenta.getTipoCuenta(), nuevaCuenta.getSaldo(), nuevaCuenta.getCodigoCliente(), nuevaCuenta.getEstado())
            
            if opt == 2:
                print('1. Modificar estado.\n2. Modificar saldo\n')
                opc = int(input('ingrese opcion: '))
                if opc == 1:
                    os.system('cls')
                    print('Modificar cliente (solo estado [0 , 1, 2, 99])')
                    id = input('ingrese codigo cuenta: ')
                    estado = int(input('ingrese nuevo estado: '))
                    nuevaConexion.modificarCuentaEstado(id, estado)
                elif opc == 2:
                    os.system('cls')
                    print('Modificar saldo cliente.')
                    id = input('ingrese codigo cuenta: ')
                    monto = int(input('ingrese nuevo monto: '))
                    nuevaConexion.modificarCuenta(id, monto)
            
            if opt == 3:
                os.system('cls')
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
                    print('movimientos')
                    nuevaConexion.verTrasaccion(id)
        if op == 3:
            print("adios")
            nuevaConexion.cerrarConexion()
            menu = False

