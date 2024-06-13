def valida_numeros(list):
        for num in list:
            try:
                int(num)
            except:
                print("Ingresó valor no valido")
                return "no valid"
        return "valid"

validador = "no valid"
while validador == "no valid":
    nums = input("Ingresa una lista de números separados por espacio")
    nums_list = nums.split() 

    validador = valida_numeros(nums_list)


