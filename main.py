from menuCliente import menuCliente
from login import loginn
from menuAdm import menuAdm


print("""
        Bienvenido a BancosShunks 1.0
     """)

usuario = loginn()
tipo = usuario[5]

if tipo == 'adm':
    menuAdm()
elif tipo == 'cliente':
    menuCliente(usuario)
else:
    print('error!')

