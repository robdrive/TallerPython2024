#ESCRIBE UN PROGRAMA QUE SOLICITE AL USUARIO UN NUMERO ENTERO Y CALCULE
#SU CUADRADO Y SU CUBO

import math

#VARIABLES

num1=int(input("Agrega un numero: "))

#OPERACIONES

cuadrado=math.pow(num1,2)
cubo=math.pow(num1,3)

#IMPRESIONES

print("El cuadrado es: ", cuadrado)
print("El cubo es: ", cubo)