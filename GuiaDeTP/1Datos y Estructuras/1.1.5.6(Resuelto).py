
"""Realizar un programa que lea dos número complejos, (a,b) y (c,d), y calcule su producto:
(a,b)∗(c,d)=(ac−db,ad+bc)"""


#solicitamos al usuario los datos del primer numero complejo
a = float(input("Ingrese la parte real del primer número compuesto: "))
b = float(input("Ingrese la parte imaginaria del primer número compuesto: "))
#solicitamos al usuario los datos del segundo numero complejo
c = float(input("Ingrese la parte real del segundo número compuesto: "))
d = float(input("Ingrese la parte imaginaria del segundo número compuesto: "))

#realizamos el calculo para ambas partes del numero complejo
parte_real = a*c-d*b
parte_imaginaria = a*d+b*c
#imprimimos
print(f"El producto entre los 2 numeros complejos es: ({parte_real},{parte_imaginaria})")