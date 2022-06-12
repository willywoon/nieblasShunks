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
        sql = 'SELECT * FROM cuentas'
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for cliente in resultado:
                print('id de cuenta:', cliente[0])
                print('tipo de cuenta:', cliente[1])
                print('saldo:', cliente[2])
                print('codigo de usuario:', cliente[3])
                print('estado cuenta (activo=1, desactivado=0):', cliente[4])
                print('------------------------------>')
            return resultado
        except Exception as e:
            raise
    
    def mostrarCuentaCodigoUsuario(self, id):
        sql = "SELECT * FROM cuentas WHERE codigousuario = '{}'".format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
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

    def modificarCuentaEstado(self,id, estado):
        sql = "UPDATE cuentas SET estado = {} WHERE idcuenta = '{}'".format(estado, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("estado modificado")
        except Exception as e:
            raise
    
    def borrarCuenta(self, id):
        sql = "DELETE FROM cuentas WHERE idcuenta = '{}'".format(id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('cuenta borrada')
        except Exception as e:
            raise

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
    
    def mostrarUnUsuario(self, id):
        sql = 'SELECT * FROM usuarios WHERE codigousuario = {}'.format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            return resultado
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

#------------transacciones------------------->

    def verTrasaccion(self, id):
        sql = "SELECT * FROM transacciones WHERE idcuenta = '{}'".format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchall()
            for transacion in resultado:
                print('id transacion: {}'.format(transacion[0]))
                print('cuenta de origen: {}'.format(transacion[1]))
                print('fecha: {}'.format(transacion[2]))
                print('cuenta de destino: {}'.format(transacion[3]))
                print('monto: {}'.format(transacion[4]))
                print('tipo: {}'.format(transacion[5]))

                print('-------------------->')
        except Exception as e:
            raise

    def ingresarTransaccion(self, idCuenta, cuentaDestino, monto, tipo):
        sql = "INSERT INTO transacciones (idcuenta, fecha, cuentadestino, monto, tipo) VALUES ('{}', CURRENT_TIMESTAMP, '{}', {}, '{}')".format(idCuenta, cuentaDestino, monto, tipo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print('transaccion registrada.')
        except:
            raise
        


