
"""Escriba un algoritmo que acepte dos números, calcule la suma e imprima el mensaje de acuerdo al
resultado obtenido.
Suma <= 50
Suma > 50 y <= 100
Suma > 100 y <= 200
Suma > 200"""


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1+num2

if suma<=50:
    print("Suma <=50")
elif suma>50 and suma<=100:
    print("Suma > 50 y <= 100")
elif suma>100 and suma<=200:
    print("Suma > 100 y <= 200")
else:
    print("Suma > 200")
