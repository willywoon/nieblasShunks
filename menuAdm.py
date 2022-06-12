import os
import random
import getpass
from winreg import REG_OPTION_BACKUP_RESTORE
from conection import Connection
from bancosShunks import Cuenta
from login import cifrar

def menuAdm():

    menu = True
    nuevaConexion = Connection()

    while menu:

        print("""

        1.- Crear Cuenta
        2.- Crear, modificar, eliminar, consultar Cliente
        3.- Salir del menú

        """)

        op = int(input('ingrese opcion: '))

        if op == 1:
            i = True
            print('Crear cuenta de usuarios (adm o cliente)')

            randomCodigoUsuario = random.randint(0, 999)
            nombre = input("ingrese nombre usuario: ")
            userLog = input("ingrese nombre usuario (para loguiar): ")
            passUsuario = getpass.getpass("ingrese password usuario (contraseña para loguaer): ")
            estado = input("ingrese estado usuario: ")

            while i:
                tipoUsuario = input("ingrese tipo usuario (adm o cliente): ")
                if tipoUsuario == 'adm' or tipoUsuario == 'cliente':
                    passCifrada = cifrar(passUsuario, 'md5')
                    i = False

            nuevaConexion.ingresarUsuario(randomCodigoUsuario, nombre, userLog, passCifrada, estado, tipoUsuario)
            print('se creo un usuario con el codigo:', randomCodigoUsuario)

            if tipoUsuario == 'cliente':

                print("creacion cliente default")
                idCuentaRandom = random.randint(0, 999)
                nuevaCuenta = Cuenta(codigoCuenta = idCuentaRandom, nombre = nombre, codigoUsuario = randomCodigoUsuario)
                print("se creo una cuenta con el codigo: {}".format(idCuentaRandom))
                nuevaConexion.ingresarCuenta(nuevaCuenta.getCodigoCuenta(), nuevaCuenta.getTipoCuenta(), nuevaCuenta.getSaldo(), nuevaCuenta.getCodigoCliente(), nuevaCuenta.getEstado())

        if op == 2:
            os.system('cls')
            print('''CRUD de cliente: 

                1.- crear nueva cuenta a un usuairio existente (cliente).
                2.- modificar cuenta.
                3.- eliminar cuenta.
                4.- consultar detalle de una cuenta o usuario. 
                5.- mostrar todas las cuentas.
            ''')

            opt = int(input('ingrese opcion: ' ))
             
            if opt == 1:
                os.system('cls')
                print('ingrese datos de la cuenta')
                codigoCuenta = random.randint(0, 999)
                i = True
                usuarios = nuevaConexion.mostrarUsuarios()
                while i:
                    codigoUsuario = input("ingrese codigo usuario (ya debe existir!): ")
                    for usuario in usuarios:
                        if codigoUsuario in usuario[0]:
                            i = False

                nuevaCuenta = Cuenta(codigoCuenta = codigoCuenta, codigoUsuario = codigoUsuario)
                nuevaConexion.ingresarCuenta(nuevaCuenta.getCodigoCuenta(), nuevaCuenta.getTipoCuenta(), nuevaCuenta.getSaldo(), nuevaCuenta.getCodigoCliente(), nuevaCuenta.getEstado())
                print("cuenta creada exitosamente con el codigo de cuenta: {}".format(nuevaCuenta.getCodigoCuenta()))

            if opt == 2:
                os.system('cls')
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
                os.system('cls')
                print('Consulta detalle de una cuenta o usuari.')
                print('1.- Cuenta.\n2.- Usuario.')
                opt = int(input('Ingrese opcion: '))
                if opt == 1:
                    os.system('cls')
                    print('Consulta de cuentas.')
                    id = input('ingrese id de la cuenta: ')
                    resultado = nuevaConexion.mostrarCuentaIdCuenta(id)
                    if resultado == None:
                        print('id cuenta no existe:')
                    else:
                        print('id cuenta es: {}, su saldo es: {} estado: {}'.format(resultado[0], resultado[2], resultado[4]))
                        print('movimientos:')
                        if nuevaConexion.verTrasaccion(id) == None:
                            print('sin movimientos--->')
                        else:
                            nuevaConexion.verTrasaccion(id)
                elif opt == 2:
                    os.system('cls')
                    print('Consulta de usuarios.')
                    id = input('ingrese codigo de usuario: ')
                    usuario = nuevaConexion.mostrarUnUsuario(id)
                    nombreUsuario = usuario[1]
                    usuarioCuentas = nuevaConexion.mostrarCuentaCodigoUsuario(id)
                    os.system('cls')
                    for cuenta in usuarioCuentas:
                        print("id cuenta:", cuenta[0])
                        print("tipo de cuenta:", cuenta[1])
                        print("saldo de la cuenta:", cuenta[2])
                        print("estado de la cuenta:", cuenta[4])
                        print('--------------------------->')
                    print('Total de cuentas del usuario: {} (codigo: {})  son {} '.format(nombreUsuario, id, len(usuarioCuentas)))
                else:
                    print('ingrese una opcion valida.')

            if opt == 5:
                os.system('cls')
                print("Mostrar todas las cuentas")
                todasLasCuentas =nuevaConexion.mostrarTodos()
                print('Total cuentas: {}'.format(len(todasLasCuentas)))
        if op == 3:
            print("adios")
            nuevaConexion.cerrarConexion()
            menu = False

