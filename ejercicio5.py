#ESCRIBE UN PROGRAMA QUE TOME UNA CALIFICACION NUMERICA ENTRE 0 Y 100 Y LE ASIGNE UNA LETRA SEGUN LA SIGUIENTE TABA:
#90-100 = A
#80-89 = B
#70-79 = C
#60-69 = D
#MENOS DE 60 = F

#VARIABLES

calificacion=int(input("Agrega una calificacion: "))

#CONDICIONALES

if calificacion>=90 and calificacion<=100:
    print("La calificacion es: A")
elif calificacion>=80:
    print("La calificacion es: B")
elif calificacion>=70:
    print("La calificacion es: C")
elif calificacion>=60:
    print("La calificacion es: D")
else:
    print("La calificacion es: F")