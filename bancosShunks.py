class Cuenta:

    #--------------constructor------------------------>

    def __init__(self, codigoCuenta = '1234', tipoCuenta = 'Vista', saldo = 0, codigoUsuario = '2342', estado = 1, nombre = 'Wonka') :
        
        self.__codigoCuenta = codigoCuenta          #idcuenta
        self.__codigoCliente = codigoUsuario
        self.__nombre = nombre 
        self.__estado = estado                           #estado 0 = desactivada, 1 = activa, 2 = transicion, 99 = cambio de estado en la papelera
        self.__saldo = saldo                            #saldo inicial 0
        self.__tipoCuenta = tipoCuenta

        #print('cliente creado')

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
  
    def consultarSaldo(self):
        if self.getEstado() == 1:
            return self.getSaldo()

    def depositar(self,monto):
        accionExitosa = False
        if self.getEstado() == 1 and monto > 0: 
            nuevoSaldo = self.getSaldo() + monto
            self.setSaldo(nuevoSaldo)
            print("depositado")
            accionExitosa = True
            return accionExitosa
        else:
            return accionExitosa

    def girar(self, monto):
        if self.getEstado() == 1 and monto <= self.getSaldo() and monto > 0: 
            nuevoSaldo = self.getSaldo() - monto
            self.setSaldo(nuevoSaldo)
            print('giro realizado')
            return True
        else:
            print("no se puede girar, saldo insuficiente :(")
            return False


