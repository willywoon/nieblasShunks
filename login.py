from traceback import print_tb
from conection import Connection


def comparacionPassYUser(pass1, pass2, user1, user2):
    if pass1 == pass2 and user1 == user2:
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

    user = input('ingrese usuario: ')
    password = input('ingrese contraseña: ')

    for usuario in listaUser:
        index = usuario.index(user)
        print(index)
    #if user in listaUser:
     #   if user.tipo == 'adm':
      #      user == listaUser
       #     return True
        #elif user.tipo =='cliente':
         #   return False
   # else:
    #    print('error usuario no encontrado')


    

loginn()