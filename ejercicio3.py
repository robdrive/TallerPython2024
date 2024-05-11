#ESCRIBA UN PROGRAMA QUE LEA UN NUMERO ENTERO Y DETERMINE SI ES POSITIVO, NEGATIVO O IGUAL A 0

#VARIABLES

num1=int(input("INGRESA UN NUMERO: "))

#OPERACIONES

if num1>0:
    print("El numero es positivo")
elif num1<0:
    print("El numero es negativo")
else:
    print("El numero es igual a 0")
