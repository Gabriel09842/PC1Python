#Problema 2:
#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
#restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
#porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
#dejar como propina

consumo = int(input('Ingrese el costo de su comida: '))
porcentaje = int(input('Porcentaje de propina que desea dejar al mesero: '))
montoFinal = round(consumo * (porcentaje/100),2)

print(f"El monto de propina es: {montoFinal} soles")


