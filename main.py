from menu import menuCliente
from login import loginn
from menu import menu2


print("""
        Bienvenido a BancosShunks 1.0
     """)


tipo = loginn()

if tipo == 'adm':
    menu2()
elif tipo == 'cliente':
    menuCliente()
else:
    print('error!')