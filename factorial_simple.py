

num = int(input("Ingrese numero entero positivo para calcular factorial: "))

def factorial(num):
    acumulador = 1
    if num < 0:
        print("Tiene que ser un numero entero positivo")
    elif num == 0:
        print("El resultado es: 1")
    else:
        for i in range(1, num+1):
            acumulador = acumulador * i
    return acumulador

print("El resultado es: ", factorial(num))

