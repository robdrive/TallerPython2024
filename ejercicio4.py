#ESCRIBE UN PROGRAMA QUE LEA UN NUMERO ENTERO Y DETERMINE SI ES DIVISIBLE ENTRE 3 Y 5

#VARIABLES

num1=int(input("Agrega un numero: "))

#OPERACIONES

if num1%3==0 and num1%5==0: #PREGUNTA SI 2 VALORES SON IGUALES, ES DIFERENTE A LA ASIGNACION (=)
    print("El numero es divisible entre 3 y 5")
else:
    print("El numero no es divisible entre 3 y 5")
