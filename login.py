from conection import Connection

def comparacionPass(pass1, pass2):
    if pass1 == pass2:
        return True
    else:
        print("contraseña no valida")
        return False

def loginn():

    db = Connection()
    listaUser = db.mostrarUsuarios()
    #print(listaUser)

    pedasitos = True
    tipo = ''

    while pedasitos:

        print("igrese usario y contraseña validos")
        user = input('ingrese usuario: ')
        password = input('ingrese contraseña: ')

        for usuario in listaUser:
            if user == usuario[2]:  
                if comparacionPass(password, usuario[3]):
                    pedasitos == False
                    tipo = usuario[5]
                    return tipo


