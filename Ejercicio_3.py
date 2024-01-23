#Problema 3:
#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
#por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado

nroPayasos = int(input('Ingrese el numero de payasos vendidos: '))
nroMuñecas = int(input('Ingrese el numero de muñecas vendidas: '))
pesoPayaso = 112
pesoMuñecas = 75
pesoFinal = (nroPayasos * pesoPayaso) + (nroMuñecas * pesoMuñecas)

print(f'El peso final del paquete es {pesoFinal}g')