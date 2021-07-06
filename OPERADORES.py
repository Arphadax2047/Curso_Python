
"""
#Suma
print(2+5)

#Restra
print(-6-5)

#Multiplicación
print((5*5)*(568*8))

#División
print(3/6)

#Módulo
print(5%2)

#Exponente
number = 5
exponente = 2
print(number**exponente)

#Floor División
print(3//6)

#Asignación
x = 10

x += 5   # x = x + 5
print(x)

x *= 2
print(x)
"""
"""
x &= 2
x |= 2
x ^= 2
x >>= 8
x <<= 5
"""

#LISTAS
#Se usan para almacenar múltiples valores o ítems en una sola variable
#Están ordenados
#Sus valores pueden cambiar
#Permite duplicidad

my_list = ["red", 2, -3.6, True, [2, 5], "orange"]
my_list_two = list(("red", "black"))
#[0 ... n]

print("Tipo de dato: ", type(my_list))
print("Mi lista: ", my_list)

print("Tamaño de mi lista: ", len(my_list))
 
print("Valor en la posición[1]:", my_list[1])

print("Valor en la posición[4][1]:", my_list[4][1])

print("Valor en la posición [4][0]:", my_list[4][0])

print("Valor en la posición[-1]: ", my_list[-1])

print("Valor en el rango 2:5", my_list[2:6])

print("Valor en el rango :4", my_list[:4])

print("Valor en el rango 4:", my_list[4:])

print("Valor en el rango -4:-1: ", my_list[-4:-1])

#Verificar que un valor está en mi lista

if "blacck" in my_list:  #True o False
    print("Si, si está dentro de la lista")
    """
    Todo el código que está aquí se ejecuta
    """
elif "rewed" not in my_list:
    print("Red está en la lista")
else:
    print("No hay nada")

###
if True:
    print()
else:
    print()

###
if True:
    print()
elif False:
    print()


my_new_list = ["Claire", "Mario", "Kirby", "Link", "Ellie"]

#Claire por Jill
print (my_new_list)
my_new_list[0] = "Jill"
print (my_new_list)

my_new_list [2:5] = ["Pikachu", "Charmander", "Charizard"]
print (my_new_list)

pokemon = ["Pikachu", "Charmander", "Charizard"]

print("\nLista pokemon")

#Charmander y Charizard por Mewtwo
pokemon [1:3] = ["MewTwo"]
print (pokemon)

#Investigar los métodos de una Lista

pokemon.insert(1, "Bulbasur")
print(pokemon)