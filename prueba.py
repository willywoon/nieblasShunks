import hashlib
import getpass
from getpass import getpass

def cifrar(valor, tipo):


    if tipo == 'sha1':

        sha1= hashlib.sha1()
        sha1.update(valor.encode('utf-8'))
        resultadoCifrado = sha1.hexdigest()
        print ("resultado de cifrado sha1:", resultadoCifrado)
        return resultadoCifrado

    elif tipo == 'md5':

        md5 = hashlib.md5(b'sinclave')
        md5.update (valor.encode ('utf-8'))
        resultadoCifrado = md5.hexdigest()
        #print("resultado de cifrado md5:", resultadoCifrado)
        return resultadoCifrado 

#x = getpass("ingresa contraseña: ")


a = cifrar("123", 'md5')
#b = cifrar(x, 'sha1')

print(a)
#print(b)