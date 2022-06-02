from conection import Connection

def loginn():

    db = Connection()
    listaUser = db.mostrarUsuarios()
    
    print("""
        Bienvenido a BancosShunks 1.0
        ingrese usuario y contraseña
     """)

    user = input('ingrese usuario: ')
    password = input('ingrese contraseña: ')

    
    (nombre)


    if user in listaUser:
        if user.tipo == 'adm':
            user == listaUser
            return True
        elif user.tipo =='cliente':
            return False
    else:
        print('error usuario no encontrado')


    

