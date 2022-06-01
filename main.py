from menu import menuCliente
from login import loginn
from menu import menu2

loginn()

if loginn():
    menu2()
elif loginn() == False:
    menuCliente()
else:
    print('error!')