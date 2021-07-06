# print --> imprime en consola

"""
primer comentrario
segundo comentario

"""
print("Hola mundo")

#Variables
# Son contenedores que almacenan un dato, valor, etc.

#Formas de declarar una variable
myvar = "Taco"
my_var = "Gato"
_my_var = "Perro"
myVar = "Cerveza"
MYVAR = "Videojuego"
myvar2 = "Cigarro"

myVariableName = "Camel case"  #Camel Case
MyVariableName = "Pascal Case" #Pascal Case
my_variable_name = "Snake Case" #Snake Case

#Formas incorrectas de declarar variables

"""
15myvar = "Valor"
my-var = "Algo"
my var = "Palabra"
"""

# Case-sensitive: distingue entre mayúsculas y minúsculas
a = "Hola"
A = "Adiós"

#Crear variables de tipo string, integer, float(decimales)

my_string = "Whisky"
my_float = 3.2
my_num = "56"

#Mi variable de tipo string es: suValor
print("Mi variable de tipo string es: " + my_string)
#print("Mi variable de tipo entero es: ", my_integer)
print("Mi variable de tipo flotantes es: ", my_float)

#print(type(my_integer))

#Cambiar el tipo de variable entero y flotante a un string
#Cambiar el tipo de variable string a un entero

# 1° --> Casting
my_integer = -10
print("**Casting**")
print("Cambio de variable de entero a string: " + str(my_integer))
#print("Cambio de variable de entero a string: " + my_integer)


# 2° --> Re-asignación de variable
my_integer = str(my_integer)  
print("Cambio de variable de entero a string: " + my_integer)
my_integer = "20"
print(type(my_integer))

print("Cambio de string a entero: ", int(my_integer))  #float()

print("\nSalto \nde \nlínea\n")

#Asignar múltiples valores a múltiples variables

color1, color2, color3 = "Rojo", "Negro", "Morado"

"""
Imprimir usando sólo un print:
El color 1 es: suValor
El color 2 es: suValor
El color 3 es: suValor
"""
"""
print("El color 1 es: "+ color1)
print("El color 2 es: "+ color2)
print("El color 3 es: "+color3)
"""

print ("El color 1 es: " + color1 + "\nEl color 2 es: " +color2 + "\nEl color 3 es: " +color3 ) 

# Asignar un mismo valor a múltiples variables

torta = "Pastor"
torta2 = torta

taco1 = taco2 = taco3 = "Suadero"
print(taco1, taco2, taco3)
#taco1 = "Suadero"
#taco2 = "Suadero"
#taco3 = "Suadero"

# Booleanos

true_var = True
falsr_var = False

print('El valor de true_var es: ', true_var)

name = "Carla"
last_name = "Zárate"

#Carla Zárate

full_name = name + " " + last_name
print(full_name) 

number1 = 4 
number2 = 8

t = str(number1) + str(number2)
print(t)

print(str(number1) + str(number2))
#48
#12
number1 = str(number1)
number2 = str(number2)
print (number1 + number2)

#¿Cuáles son los operadores aritméticos de Python?
#¿Cuáles son los operadores de asignación de Python?
#Ejemplo de cada uno

print("Operador de adición +: ", 25+10)

x = 5
x += 2    # x = x + 2

print(x)