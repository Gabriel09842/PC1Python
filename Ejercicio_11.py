#Problema 11:
#Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
#lista. Su programa debe retornar otra lista sin los duplicados.
#Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
#Lista procesada: [1, 2, 3, 4,, 5]

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_procesada = []

for elemento in lista_original:
    if elemento not in lista_procesada:
        lista_procesada.append(elemento)

print(lista_procesada)

