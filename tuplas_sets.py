

list = ["manzana", "pera"]

list.append("naranja")
list.append("banana")

print(list)

tuple_1 = tuple(list)

list.append("pineapple")

print(tuple_1)
print("Cantidad de elementos en tupla", len(tuple_1))

print("el tipo de dato de las tuplas es: ", type(tuple_1))
print(list)

lista_2 = [i for i in tuple_1] ##Convierto tupla en lista con lists comprehensions

print("Lista 2", lista_2)
