"""

Puedes usar elif (abreviatura de "else if")
para verificar múltiples condiciones
ya que con el if else solo se verificaba una condicion

Es util cuando se manejan mas de dos opciones
o se tienen que considerar mas casos

"""

numero=int(input('Ingrese un numero: '))

"""
Para esta situacion se manejan 3 posibles resultados; que el numero sea,
    positivo
    negativo o
    cero
resultados que por si solos el if else no manejan pues solamente
verificaria una condicion que produciría dos casos posibles

"""

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")


"""
Indentación: En Python, es crucial mantener la indentación adecuada,
ya que esta determina qué bloques de código están asociados con cada condición.

"""