
"""1. Hacer un algoritmo que calcule la altura aproximada de un edificio en pies, ingresando como
dato la cantidad de pisos del mismo y la altura promedio de cada piso, en metros. (1 m = 3.28 pies)
2. Modifique el algoritmo del punto 1. para que permita calcular la altura de 50 edificios.
3. Modifique el algoritmo del punto 1. para que permita calcular la altura de una cantidad
indeterminada de edificios. Prevea una condición de fin."""


pisos = float(input("Ingrese la cantidad de pisos del edificio: "))
altura_p = float(input("Ingrese la altura promedio de los pisos del edificio: "))

print(f"La altura aproximada del edificio es de: {(pisos*altura_p)*3.28}")