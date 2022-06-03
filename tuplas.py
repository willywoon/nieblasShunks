from bancosShunks import Cuenta

w = Cuenta(saldo=1000000)

print(w.consultarSaldo())

w.girar(100)

print(w.consultarSaldo())
