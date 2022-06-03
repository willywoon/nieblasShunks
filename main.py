from menu import menuCliente
from login import loginn
from menu import menuAdministrador


print("""
        Bienvenido a BancosShunks 1.0
     """)

usuario = loginn()
tipo = usuario[5]

if tipo == 'adm':
    menuAdministrador()
elif tipo == 'cliente':
    menuCliente(usuario)
else:
    print('error!')

