
nombres = []
large = ""
for i in range(3):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    if len(nombre) > len(large):
        large = nombre
        
print("El nombre más extenso ingresado es: ", large)
    

