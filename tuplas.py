a = ("dato1", "dato2")
b = ("dato3", "dato4")

c= (a, b)


for elemento in c:

    if elemento[0] == "dato3":
        print(elemento[1])