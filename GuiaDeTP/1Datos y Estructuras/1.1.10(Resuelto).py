
"""Dados dos números enteros A y B generar un algoritmo que permita determinar si A es divisor de
B o B es divisor de A."""


a = float(input("Ingrese un número entero llamado A: "))
b = float(input("Ingrese otro número entero llamado B: "))

if ((a%b)==0):
    print("A es divisor de B")
elif ((b%a)==0):
    print("B es divisor de A")
else:
    print("A y B No son divisores")
