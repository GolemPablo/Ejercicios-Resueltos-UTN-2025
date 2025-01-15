
"""Escriba un algoritmo que permita ingresar 3 valores numéricos y determine cuál es el mayor, el
medio y el menor."""

#solicitamos los valores al usuario
valor1 = float(input("Ingrese 3 numeros, cada uno seguido de presionar la tecla enter: "))
valor2 = float(input())
valor3 = float(input())


if valor1 >= valor2 >= valor3 or valor1 >= valor3 >= valor2: #comprobamos si el valor 1 es el mayor
    mayor = valor1
    menor = min(valor2, valor3)
    medio = max(valor2, valor3)
elif valor2 >= valor1 >= valor3 or valor2 >= valor3 >= valor1: #comprobamos si el valor 2 es el mayor
    mayor = valor2
    menor = min(valor1, valor3)
    medio = max(valor1, valor3)
else:
    mayor = valor3 #en caso de que las condiciones anteriores sean falas, damos por sentado que la opcion 3 es la de mayor valor
    menor = min(valor1, valor2)
    medio = max(valor1, valor2)
#imprimimos
print(f"El mayor es: {mayor}, el medio es: {medio}, el menor es: {menor}")