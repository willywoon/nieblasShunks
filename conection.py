import pymysql, os
os.system('cls')

class Connection:

    def __init__(self):

        self.connection = pymysql.connect(
            db = 'bancosshunks',
            host = 'localhost',
            user = 'root',
            passwd = ''
        )

        self.cursor = self.connection.cursor()
        print('conexion establecida------------------->')

#-------------------clientes----------------->

    def mostrarTodos(self):
        sql = 'SELECT * FROM clientes'
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for cliente in resultado:
                print(cliente)
        except Exception as e:
            raise
    
    def mostrarCuentaCodigoUsuario(self, id):
        sql = "SELECT * FROM cuentas WHERE codigousuario = '{}'".format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as e:
            raise

    def mostrarCuentaIdCuenta(self, id):
        sql = "SELECT * FROM cuentas WHERE idcuenta = '{}'".format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            return resultado
        except Exception as e:
            raise

    def modificarCuenta(self,id, monto):
        sql = "UPDATE cuentas SET saldo = {} WHERE idcuenta = '{}'".format(monto, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("saldo modificado")
        except Exception as e:
            raise
    
    def borrarCuenta(self):
        pass

    def ingresarCuenta(self, idcuenta, tipocuenta, saldo, codigoUsuario, estado):
        sql = "INSERT INTO cuentas (idcuenta, tipocuenta, saldo, codigousuario, estado) VALUE ('{}', '{}', '{}', '{}', {})".format(idcuenta, tipocuenta, saldo, codigoUsuario, estado)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("cuenta ingresada")
        except Exception as e:
            raise

#------------usuarios------------------->

    def ingresarUsuario(self, codigoUsuario, nombreCliente, nombreUsuario, password, estado, tipo):
        sql = "INSERT INTO usuarios (codigousuario, nombrecliente, nombreusuario, password, estado, tipousuario) VALUE ('{}', '{}', '{}', '{}', {}, '{}')".format(codigoUsuario, nombreCliente, nombreUsuario, password, estado, tipo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("usuario ingresado :)")
        except Exception as e:
            raise

    def mostrarUsuarios(self):
        sql = "SELECT * FROM usuarios"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            return resultado
        except Exception as e: 
            raise

    def cerrarConexion(self):
        self.connection.close()
        print('conexion cerrada!')

#nw = Connection()
#nw.ingresarUsuario('sasdhs', 'vista', 0, '18728y', '715681', 1)
#nw = Connection()
#nw.ingresarUsuario('ggsefg', 'LunaAdm', 'mushweunga', '12we3456', 1, 'adm')
#nw.ingresarUsuario('kdjf34', 'Luna', 'mushunga', '123456', 1, 'cliente')

#nw.modificarCuenta(234, 100)