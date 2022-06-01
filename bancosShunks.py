class Cliente:

    #--------------constructor------------------------>


    def __init__(self, codigoCuenta = '1234', codigoCliente = '2342', nombre = 'Wonka', idUsuario = 'defaul') :
        
        self.__codigoCuenta = codigoCuenta          #idcuenta
        self.__codigoCliente = codigoCliente
        self.__nombre = nombre 
        self.__estado = 1                           #estado 0 = desactivada, 1 = activa, 2 = transicion, 99 = cambio de estado en la papelera
        self.__saldo = 0                            #saldo inicial 0
        self.__tipoCuenta = 'Vista'
        self.__idUsuario = idUsuario

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

    def getIdUsuario(self):
        return self.__idUsuario
        
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
            return True
        else:
            return False

'''
nuevoCliente = Cliente('2323', '35')
print(nuevoCliente.consultarSaldo())
nuevoCliente.depositar(1000)
print(nuevoCliente.girar(200))
print(nuevoCliente.consultarSaldo())
'''
