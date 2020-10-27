#VARIABLE GLOBAL
vglobal = "mi Variable global"

#Python usa sangría para indicar un bloque de código.
if 5 > 2:
    print("Five is greater than two!")

#Python le dará un error si omite la sangría:
#if 5 > 2:
#print("Five is greater than two!")

#El número de espacios depende de usted como programador, pero debe ser al menos uno.
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
            print("Five is greater than two!") 

#Tienes que usar la misma cantidad de espacios en el mismo bloque de código, de lo contrario Python te dará un error:
#if 5 > 2:
#    print("Five is greater than two!")
#            print("Five is greater than two!")

#Python no tiene ningún comando para declarar una variable.
mivariable = 0
x = 5
y = "Hello, World!"

x1 = 5
y2 = "John"
print(x1)
print(y2)

#Las variables no necesitan declararse con ningún tipo en particular e incluso pueden cambiar de tipo después de que se hayan establecido.
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

vglobal = 1

#Las variables de cadena se pueden declarar utilizando comillas simples o dobles:
x = "John"
# is the same as
x = 'John ---'

print(x)

'''
El nombre de una variable debe comenzar con una letra o el carácter de subrayado
Un nombre de variable no puede comenzar con un número
El nombre de una variable solo puede contener caracteres alfanuméricos y guiones bajos (Az, 0-9 y _)
Los nombres de las variables distinguen entre mayúsculas y minúsculas (la edad, la Edad y la eDad son tres variables diferentes)
'''

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Illegal variable names:
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''

#Asignar valor a múltiples variables
#Python le permite asignar valores a múltiples variables en una línea:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Y puede asignar el mismo valor a múltiples variables en una línea:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Variables de salida
#La print declaración de Python se usa a menudo para generar variables.

#Para combinar texto y una variable, Python usa el + carácter:
x = "awesome"
print("Python is " + x)

#Para los números, el +carácter funciona como operador matemático:
x = 5
y = 10
print(x + y)

vglobal = "Hola python basico C"

'''
#Si intenta combinar una cadena y un número, Python le dará un error:
x = 5
y = "John"
print(x + y)
'''
#Para combinar texto y Enteros en variables, Python usa el carácter: ' , '
x = 5
y = "John tiene:"
z = "Anios"
print(y , x , z)

#Variables globales
#Las variables que se crean fuera de una función (como en todos los ejemplos anteriores) se conocen como variables globales.
#Todo el mundo puede utilizar las variables globales, tanto dentro como fuera de las funciones



def myfunc():
  print( vglobal )

myfunc()
