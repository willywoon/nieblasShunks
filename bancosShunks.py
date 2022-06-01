class Cliente:

    def __init__(self, codigoCuenta = '1234', codigoCliente = '2342', nombre = 'Wonka'):
        
        self.__codigoCuenta = codigoCuenta
        self.__codigoCliente = codigoCliente
        self.__nombre = nombre 
        self.__estado = True
        self.__saldo = 0
        self.__tipoCuenta = 'Vista'

        print('cliente creado')

    #--------------gestters------------------------>
    
    def getNombre(self):
        return self.__nombre
    
    def getCodigoCuenta(self):
        return self.__codigoCuenta
    
    def getCodigoCliente(self):
        return self.__codigoCliente
    
    def getEstado(self):
        return self.__estado
    
    def getSaldo(self):
        return self.__saldo

    def getTipoCuenta(self):
        return self.__tipoCuenta

    #--------------setters------------------------>

    def setNombre(self, newNombre):
        self.__nombre = newNombre
    
    def setCodigoCuenta(self, newCodigo):
        self.__codigoCuenta = newCodigo
    
    def setCodigoCliente(self, newCodigo):
        self.__codigoCliente = newCodigo
    
    def setEstado(self, newEstado):
        self.__estado = newEstado
    
    def setSaldo(self, newSaldo):
        self.__saldo = newSaldo

    def setTipoCuenta(self, newTipo):
        self.__tipoCuenta = newTipo

    #--------------functions------------------------>
  
    def consultarSaldo():
        pass

nuevoCliente = Cliente('2323', '35')