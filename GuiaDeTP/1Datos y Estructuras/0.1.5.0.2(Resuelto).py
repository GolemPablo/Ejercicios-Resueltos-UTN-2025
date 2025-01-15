
"""Diseñe un algoritmo que permita resolver el siguiente enunciado:
2- Convertir una suma en dólares a PESOS. Se debe prever que el valor de conversión puede cambiar."""


dolar_precio_en_pesos = float(input("Ingrese el valor del dolar en pesos al momento en el que realiza la conversion: "))
cantidad_dolar = float(input("Ingrese la cantidad de dolares que desea convertir: "))

print(f"La cantidad de {cantidad_dolar}USD convertidos a pesos da un valor de: ${dolar_precio_en_pesos*cantidad_dolar}")
