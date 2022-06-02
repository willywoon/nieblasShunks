from traceback import print_tb
from conection import Connection


def comparacionPass(pass1, pass2):
    if pass1 == pass2:
        return True
    else:
        return False

def loginn():

    db = Connection()
    listaUser = db.mostrarUsuarios()
    print(listaUser)

    
    print("""
        Bienvenido a BancosShunks 1.0
        ingrese usuario y contraseña
     """)

     while 

    user = input('ingrese usuario: ')
    password = input('ingrese contraseña: ')

    for usuario in listaUser:
        if user == usuario[0]:  
            if comparacionPass(password, usuario[3]):
                pass
    #if user in listaUser:
     #   if user.tipo == 'adm':
      #      user == listaUser
       #     return True
        #elif user.tipo =='cliente':
         #   return False
   # else:
    #    print('error usuario no encontrado')


    

loginn()