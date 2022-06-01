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
        
        sql = 'SELECT * FROM cuentas WHERE idcliente = {}'.format(id)
        try:
            self.cursor.execute(sql)
            resultado = self.cursor.fetchone()
            print(resultado)
        except Exception as e:
            raise
        finally:
            self.connection.close()

    def modificarElemento(self):
        pass

    def borrarElemento(self):
        pass

    def ingresarElemento(self, idcuenta, tipocuenta, saldo, idcliente, idusario):
        sql = 'INSERT INTO cuentas (idcuenta, tipocuenta, saldo, idcliente, idusario) VALUE ({}, {}, {}, {}, {})'.format(idcuenta, tipocuenta, saldo, idcliente, idusario)