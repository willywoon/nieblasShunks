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
        
        sql = "SELECT * FROM cuentas WHERE idcliente = '{}'".format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            print(resultado)
        except Exception as e:
            raise
        finally:
            self.connection.close()

    def modificarElemento(self,id, estado):
        sql = "UPDATE cuentas SET estado = {} WHERE idcliente = '{}'".format(estado, id)
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
        sql = "INSERT INTO cuentas (idcuenta, codigocliente, tipocuenta, saldo, idusuario, estado) VALUE ('{}', '{}', '{}', '{}', '{}', {})".format(idcuenta, codigoCliente, tipocuenta, saldo, idusuario, estado)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise
        finally:
            self.connection.close()


#nw = Connection()
#nw.ingresarCliente('sasdhs', 'vista', 0, '18728y', '715681', 1)