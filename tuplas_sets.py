
tupla_0 = ("Javier","Oscar","Pedro")
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

##Podemos recorrer una tupla igual que una lista
for fruta in tuple_1:
    print(fruta)

print(tuple_1[1:4])
print(tupla_0)

tupla_4 = tupla_0 + tuple_1
print(tupla_4)
#Contando la cantidad de veces que aperece un elemento en la tupla
print(tupla_4.count("manzana"))

#Muestra el índicia (posición) donde se encuentra el elemento buscado
print(tupla_4.index("Pedro"))

print((tupla_0,tupla_4))

###############################################
###                 SETS                    ###
###############################################

thisset = {"apple","cherry", "banana",  "apple"}

set_2 = thisset

print(set_2)

set_2.add("pineapple")
print(set_2)
set_2.add("pineapple")
print(set_2)

for fruit in set_2:
    print(fruit)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya","apple"}

thisset.update(tropical)

print(thisset)

thisset.remove("banana")

print(thisset)

matrix_set = thisset

print(matrix_set)

set_de_lista = set(lista_2)

print(set_de_lista)

