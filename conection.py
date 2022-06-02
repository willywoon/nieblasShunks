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
        finally:
            self.connection.close()
    
    def mostrarCliente(self, id):
        sql = "SELECT * FROM cuentas WHERE idcuenta = '{}'".format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
        except Exception as e:
            raise
        finally:
            self.connection.close()
            return resultado

    def modificarElemento(self,id, estado):
        sql = "UPDATE cuentas SET estado = {} WHERE idcuenta = '{}'".format(estado, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        finally:
            self.connection.close()
    
    def borrarElemento(self):
        pass

    def ingresarCliente(self, idcuenta, tipocuenta, saldo, codigoCliente, idusuario, estado):
        sql = "INSERT INTO cuentas (idcuenta, codigocliente, tipocuenta, saldo, estado) VALUE ('{}', '{}', '{}', '{}', {})".format(idcuenta, codigoCliente, tipocuenta, saldo, idusuario, estado)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        finally:
            self.connection.close()


#------------usuarios------------------->

    def ingresarUsuario(self, codigoUsuario, nombreCliente, nombreUsuario, password, estado, tipo):
        sql = "INSERT INTO usuarios (codigousuario, nombrecliente, nombreusuario, password, estado, tipousuario) VALUE ('{}', '{}', '{}', '{}', {}, '{}')".format(codigoUsuario, nombreCliente, nombreUsuario, password, estado, tipo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def mostrarUsuarios(self):
        sql = "SELECT nombreUsuario, password, tipousuario  FROM usuarios"
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            return resultado
        except Exception as e: 
            raise


    def cerrarConexion(self):
        self.connection.close()

#nw = Connection()
#nw.ingresarUsuario('sasdhs', 'vista', 0, '18728y', '715681', 1)
#nw = Connection()
#nw.ingresarUsuario('ggsefg', 'LunaAdm', 'mushweunga', '12we3456', 1, 'adm')
#nw.ingresarUsuario('kdjf34', 'Luna', 'mushunga', '123456', 1, 'cliente')