#ESCRIBE UN PROGRAMA QUE SOLICITE AL USUARIO 3 NUMEROS Y DETERMINE CUAL DE ELLOS ES EL MAYOR

#VARIABLES

num1=int(input("Agrega un numero: "))
num2=int(input("Agrega otro numero: "))
num3=int(input("Agrega el ultimo numero: "))

#OPERACIONES

if num1>num2 and num1>num3:
    print("El numero mayor es: ", num1)
elif num2>num1 and num2>num3:
    print("El numero mayor es: ", num2)
else:
    print("El numero mayor es: ", num3)
