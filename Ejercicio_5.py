#Problema 5:
#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows

nroShows = int(input('Ingresa la cantidad de shows musicales que has visto en el ultimo año: '))
verificar = nroShows > 3
print(verificar)
