#Para entender los bucles for al estilo python
#es clave primero entender la funcion range() 

#¿Por qué range() es tan importante?
#Porque es la forma más directa de hacer "bucle por contador" en Python

#¿Qué es range()?
#Es una función que genera una secuencia de números, uno por uno,
#sin crear una lista completa en memoria (es un iterable tipo generador).

#Sintaxis de range()
#   - range(fin)                      # Desde 0 hasta fin - 1
#   - range(inicio, fin)              # Desde inicio hasta fin - 1
#   - range(inicio, fin, paso)        # Desde inicio hasta fin - 1 en pasos de 'paso'

#fin - 1 es una manera rapida de decir que el range() en realidad
#va desde inicio hasta justo antes de fin

#range() devuelve un objeto iterable, es decir, una secuencia perezosa (lazy)
#que genera los números uno a uno.


#Y la manera de acceder a esa secuencia de numeros generados
#es mediante el bucle for y funciona de la siguiente forma
#Se designa una variable que va almacenar los numeros de la secuencia
#Esta variable va tomar sucesivamente los numeros generados por range()
#desde inicio hasta fin-1

#Observación: el for es la forma más común, pero no la única de acceder
#a los números generados por range(),
#   1. Convertirlo en lista (forzado en memoria)
#   2. Acceder por índice
#   3. Usar slicing (rebanado)
#   4. Usar funciones como sum(), max(), min()

#Porque range no es un iterador directamente,
#sino un iterable. Si querés recorrerlo manualmente,
#primero necesitás hacer un iterador.

#Sintaxis: for variable in range(inicio, fin, paso)

for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

print("-----")

for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

print("-----")

for i in range(10, 0, -2):     #como el fin es 0, el range va hasta
                               #justo antes de 0 
    print(i)  # 10, 8, 6, 4, 2 #El rango comienza en 10 y se
                               #detiene justo antes de llegar a 0

#De esta forma se construye el bucle for en Python.
#Podemos ver que 'for' no se limita a un caso específico,
#sino que se adapta a cualquier situación donde haya algo iterable.



