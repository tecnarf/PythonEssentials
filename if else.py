"""
Las estructuras if y else en Python 
permiten ejecutar diferentes bloques de código
según si una condición es verdadera o falsa.

"""


# Inicializamos una variable
numero = int(input('Ingresa un numero: '))

# Usamos if y else para verificar si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")


    
"""
Condición if: La condición numero % 2 == 0 verifica si el número es divisible
entre 2 (es decir, si es par).

Bloque if: Si la condición es verdadera, se ejecuta el bloque de código
dentro del if, imprimiendo que el número es par.

Bloque else: Si la condición es falsa (es decir, el número es impar),
se ejecuta el bloque de código dentro del else,
imprimiendo que el número es impar.

"""

