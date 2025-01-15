
"""Escriba un algoritmo que permita ingresar 3 valores numéricos y determine cuál es el mayor, el
medio y el menor."""


valor1 = float(input("Ingrese 3 numeros, cada uno seguido de presionar la tecla enter: "))
valor2 = float(input())
valor3 = float(input())

if valor1 >= valor2 >= valor3 or valor1 >= valor3 >= valor2:
    mayor = valor1
    menor = min(valor2, valor3)
    medio = max(valor2, valor3)
elif valor2 >= valor1 >= valor3 or valor2 >= valor3 >= valor1:
    mayor = valor2
    menor = min(valor1, valor3)
    medio = max(valor1, valor3)
else:
    mayor = valor3
    menor = min(valor1, valor2)
    medio = max(valor1, valor2)

print(f"El mayor es: {mayor}, el medio es: {medio}, el menor es: {menor}")