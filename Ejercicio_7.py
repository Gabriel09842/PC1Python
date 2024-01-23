#Problema 7:
#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

n1 = int(input('Ingrese el primer numero: '))
n2 = int(input('Ingrese el segundo numero: '))
print("""-------------------Menu-------------------
a) Mostrar una suma de los dos números
b) Mostrar una resta de los dos números (el primero menos el segundo)
c) Mostrar una multiplicación de los dos números""")
opcion = input('Elija una opcion: ')

if opcion == 'a':
    print(n1 + n2)
elif opcion == 'b':
    print(n1 - n2)
elif opcion == 'c':
    print(n1 * n2)
else:
    print("Opcion no valida")

