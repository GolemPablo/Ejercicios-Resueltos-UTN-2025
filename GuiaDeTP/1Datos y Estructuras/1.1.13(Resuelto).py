
"""Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000 que representa una
suma de dinero e indique cuantos billetes de cada denominación necesita, suponiendo que solo
existen billetes de 100, 10 y 1 peso."""


pesos = int(input("Ingrese una cantidad de dinero mayor a $100 y menor a $1000: "))
while pesos >= 1000 or pesos <= 100:
    pesos = int(input("Incorrecto, por favor ingrese una cantidad de dinero mayor a $100 y menor a $1000: "))

if pesos >= 100:
    billetes_100 = pesos // 100
    print(f"Usted necesita {billetes_100} {'billete' if billetes_100 == 1 else 'billetes'} de $100")
    pesos %= 100

if pesos >= 10:
    billetes_10 = pesos // 10
    print(f"Usted necesita {billetes_10} {'billete' if billetes_10 == 1 else 'billetes'} de $10")
    pesos %= 10

if pesos > 0:
    print(f"Usted necesita {pesos} {'billete' if pesos == 1 else 'billetes'} de $1")
