nombres = []
apellidos = []
for i in range(3):
    nombre = input("Ingrese un nombre: ")
    apellido = input("Ingrese un apellido: ")
    nombres.append(nombre)
    apellidos.append(apellido)

nombres.sort()
apellidos.sort()

print("Nombres ordenados: {}, {}, {} ".format(nombres[0], nombres[1], nombres[2]))
print("Apellidos ordenados: {}, {}, {} ".format(apellidos[0], apellidos[1], apellidos[2]))