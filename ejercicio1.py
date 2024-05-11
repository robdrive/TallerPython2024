#ESCRIBE UN PROGRAMA QUE SOLICITE AL USUARIO 2 NUMEROS Y MUESTRE SU SUMA
#RESTA, MULTIPLICACION, DIVISION, DIVISION ENTERA Y RESIDUO.

#VARIABLES

num1=int(input("INGRESA UN NUMERO: "))
num2=int(input("INGRESA OTRO NUMERO: "))

#OPERADORES ARITMETICOS

suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=num1/num2
divisionEntera=num1//num2 #SE USA // PARA UNA DIVISION SIN NUMEROS DECIMALES, ES UN NUMERO ENTERO EL RESULTADO
residuo=num1%num2

#IMPRESIONES

print("La suma es: ", suma)
print("La resta es: ", resta)
print("la multiplicacion es: ", multiplicacion)
print("La division es: ", division)
print("La division entera es: ", divisionEntera)
print("El residuo es: ", residuo)

