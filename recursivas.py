
def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

num = int(input("Ingrese numero entero positivo para calcular factorial: "))
print(factorial(num))