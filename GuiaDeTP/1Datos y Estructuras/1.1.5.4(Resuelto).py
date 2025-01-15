
"""Se desea calcular la superficie de un trapecio, para la cual se ingresa la longitud de ambas
bases y la altura. Finalizando el proceso, emitir dicha superficie y los valores ingresados."""


base_1 = float(input("Ingrese el valor de la base inferior del trapecio: "))
base_2 = float(input("Ingrese el valor de la base superior del trapecio: "))
altura = float(input("Ingrese el valor de la altura de l trapecio: "))
medicion = input("Declara en que sistema de unidad están expresadas las medidas: ")

superficie = ((base_1+base_2)*altura)/2

print(f"La superficie del trapecio es de: {superficie} {medicion}")
