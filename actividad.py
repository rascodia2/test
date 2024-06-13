def valida_numeros(list):
        for num in list:
            try:
                int(num)
            except:
                print("Ingresó valor no valido")
                return False
        return True

numbers_list = ["a"]
while not valida_numeros(numbers_list):

    numbers = input("Ingrese numeros separados por espacio: ")
    numbers_list = numbers.split()

print(numbers_list)