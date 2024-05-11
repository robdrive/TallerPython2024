#DECLARACION DE MATH
import math
#VARIABLES
num1=int(input("Agrega numero 1: "))
num2=int(input("Agrega numero 2: "))
#OPERACIONES ARITMETICAS
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=num2/num1
operacion=(num1+num2)*multiplicacion
potencia=num1**2 #DOBLES ** SIRVEN PARA DECLARAR POTENCIAS
potencia2=math.pow(num2,3) #PARA USAR ESTA FUNCION A INICIO DEL PROGRAMA DEBES DECLARAR MATH
raiz=math.sqrt(num1)
raiz3=num2**1/3
residuo=num1%num2 #USAR EL SIMBOLO % SIRVE PARA MOSTRAR EL RESIDUO DE UNA DIVISION
#REDONDEO DE DECIMALES DE UN NUMERO
num3=float(input("Agrega un numero decimal: ")) #FLOAT SIRVE PARA DEFINIR QUE UN NUMERO VA A TRAER DECIMALES
num3R=round(num3,2) #ROUND SIRVE PARA REDONDEAR UN NUMERO A LOS DECIMALES QUE PONGAS
#IMPRESION DE DATOS
print("El resultado de la suma es: ", suma) #LA COMA (,) SIRVE PARA JUNTAR EL STRING Y LA SUMA
print("El resultado de la resta es: ", resta)
print("El resultado de la multiplicacion es: ", multiplicacion)
print("El resultado de la division es: ", division)
print("El resultado de la operacion es: ", operacion)
print("El resultado de la potencia del numero 1 es: ", potencia)
print("El resultado de la potencia del numero 2 es: ", potencia2)
print("El resultado de la raiz cuadrada es: ", raiz)
print("El resultado de la raiz cubica es: ", raiz3)
print("El residuo es: ", residuo)
print("Tu numero es: ", num3)
print("Tu numero redondeado es: ", num3R)