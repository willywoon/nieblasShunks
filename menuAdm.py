import os
import random
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
            control = True
            print('Crear cuenta de usuarios (adm o cliente)')
            randomCodigoUsuario = random.randint(0, 999)
            b = input("ingrese nombre cliente: ")
            c = input("ingrese nombre usuario (para loguiar): ")
            passUsuario = input("ingrese password usuario (contraseña para loguaer): ")
            e = input("ingrese  estado usuario: ")
            while control:
                tipoUsuario = input("ingrese tipo usuario (adm o cliente): ")
                if tipoUsuario == 'adm' or tipoUsuario == 'cliente':
                    passCifrada = cifrar(passUsuario, 'md5')
                    control = False

            nuevaConexion.ingresarUsuario(randomCodigoUsuario, b, c, passCifrada, e, tipoUsuario)

            if tipoUsuario == 'cliente':

                print("creacion cliente default")
                idCuentaRandom = random.randint(0, 999)
                nuevaCuenta = Cuenta(codigoCuenta = idCuentaRandom, nombre = b, codigoUsuario = randomCodigoUsuario)
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
                    print('id cuenta es: {}, su saldo es: {} estado: {}'.format(resultado[0], resultado[2], resultado[4]))
                    print('movimientos:')
                    if nuevaConexion.verTrasaccion(id) == None:
                        print('sin movimientos--->')
                    else:
                        nuevaConexion.verTrasaccion(id)
        if op == 3:
            print("adios")
            nuevaConexion.cerrarConexion()
            menu = False



menuAdm()