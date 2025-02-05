"""
En Python, las palabras clave break y continue se utilizan
para controlar el flujo de los bucles (for o while).

"""

"""
La instrucción break se utiliza para salir inmediatamente de un bucle,
sin importar si quedan iteraciones por completar.
Cuando Python encuentra un break, el bucle se termina y
el control del programa continúa con la siguiente
línea después del bucle.

"""

for numero in range(1, 10): #recordemos que numero guarda cada paso
                            #o iteracion del bucle, es el iterador
    if numero == 5:
        print("¡Se alcanzó el número 5, terminando el bucle!")
        break  # Sale del bucle cuando llega al número 5
    print(f"Numero: {numero}")

#En este caso, el bucle termina inmediatamente
#cuando el número es igual a 5.


# Salida:
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# ¡Se alcanzó el número 5, terminando el bucle!



"""
La instrucción continue se utiliza para omitir el resto del código
en la iteración actual del bucle y pasar directamente a la siguiente
iteración. A diferencia de break, el bucle no se detiene,
solo salta esa iteración específica.

"""

for numero in range(1, 10):
    if numero == 5:
        print("Saltando el número 5")
        continue  #Salta el resto del código para esta iteración
        #las lineas de codigo que esten debajo de continue se omiten
        print("esta linea de codigo no se ejecuta")
    print(f"Número: {numero}")


"""

En este caso, cuando el número es 5, se imprime "Saltando el número 5"
y se omite el print(f"Número: {numero}"), es decir,
no se imprime Numero: 5, continuando con la siguiente
iteración.

"""

# Salida:
# Número: 1
# Número: 2
# Número: 3
# Número: 4
# Saltando el número 5
# Número: 6
# Número: 7
# Número: 8
# Número: 9
