"""
Un bucle o ciclo, en programación, es una secuencia de instrucciones
que se ejecuta repetidas veces,
hasta que la condición asignada a dicho bucle deja de cumplirse.
El while en Python se utiliza para ejecutar un bloque de instrucciones
repetidamente mientras una condición especificada sea verdadera.

"""
#inicializamos una variable
contador = 0
#usamos un bucle while para contar hasta 5
while contador < 5:
    print(f"Contador: {contador}")
    contador = contador + 1 #se incrementa el valor
    #aqui termina la ejecucion del bloque de instrucciones
    #pero como esta dentro de un while
    #no se pasara a la siguiente instruccion (que esta fuera del while)
    #hasta que contador < 5 sea falso
print("el bucle ha finalizado")
