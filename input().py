"""
En python, input() siempre devuelve cadenas de texto (strings);
todo lo que se ingrese por medio de input() sera interpretado como
cadena de texto (string) por lo que a la variable se le asignara un string

"""
nombre = input("como te llamas? ")
saludo = "Hola"
print(saludo + nombre)


"""
Cuando se hace saludo + nombre, se esta concatenando esas cadenas.
Para sumar los valores como números, se debe convertir las entradas
a tipos numéricos (como int o float) antes de realizar la operación.
"""

a = int(input("ingrese un valor para a = "))
b = int(input("ingrese un valor para b = "))
print(f"la suma es a+b = {a+b}") #otra forma de imprimir enn pantalla


"""
Ahora cuando se hace a + b, se esta sumando valores numéricos.

"""
