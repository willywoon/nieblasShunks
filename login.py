def loginn():
    
    print("""
        Bienvenido a BancosShunks 1.0
        ingrese usuario y contraseña
     """)

    user = input('ingrese usuario: ')
    password = input('ingrese contraseña: ')

    if user in listaUsers:
        if user.tipo == 'adm':
            return True
        elif user.tipo =='cliente':
            return False
    else:
        print('error usuario no encontrado')


    

