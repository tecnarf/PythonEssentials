#Escribir un programa que reciba del usuario el radio de un círculo y calcule e imprima el perimetro y el área
#correspondiente.


print("-------------------------------------------")
print("Calculo del perimetro y area de un circulo")
print("-------------------------------------------")

pi=3.14 #constante
#print(type(pi))

radio = float(input("Ingrese el radio del circulo: r = "))#transformamos la variable que inicialmente es un string a un float
#print(type(radio))

perimetro = 2*pi*radio
area=pi*radio**2 #potenciacion en python

print("El perimetro es: ", perimetro)
print("El area es: ", area)
