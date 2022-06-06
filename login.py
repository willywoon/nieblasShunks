import hashlib
from conection import Connection

def cifrar(valor, tipo):

    if tipo == 'sha1':

        sha1= hashlib.sha1()
        sha1.update(valor.encode('utf-8'))
        resultadoCifrado = sha1.hexdigest()
        #print ("resultado de cifrado sha1:", resultadoCifrado)
        return resultadoCifrado

    elif tipo == 'md5':

        md5 = hashlib.md5()
        md5.update (valor.encode ('utf-8'))
        resultadoCifrado = md5.hexdigest()
        #print("resultado de cifrado md5:", resultadoCifrado)
        return resultadoCifrado

#b = cifrar('1313', 'md5')
#print(b)

def comparacionPass(pass1, pass2):
    if pass1 == pass2:
        return True
    else:
        print("contraseña no valida")
        return False

def loginn():

    db = Connection()
    listaUser = db.mostrarUsuarios()

    pedasitos = True

    while pedasitos:

        print("ingrese usario y contraseña validos")
        user = input('ingrese usuario: ')
        password = input('ingrese contraseña: ')
        # transformar --------->
        passCifrada = cifrar(password, 'md5')

        for usuario in listaUser:
            if user == usuario[2]:  
                if comparacionPass(passCifrada, usuario[3]):
                    pedasitos == False
                    return usuario


