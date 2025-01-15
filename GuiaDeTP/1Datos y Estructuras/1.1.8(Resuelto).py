
"""Escriba un algoritmo que permita conocer la edad de una persona, con solo ingresar la fecha de
nacimiento y la fecha actual, ambas en el formato: DIA, MES, AÑO"""

#solicitamos la fecha de nacimiento del usuario
dia = float(input("Ingrese el día de su nacimiento: "))
mes = float(input("Ingrese el mes de su naciemiento: "))
anio = float(input("Ingrese el año de su nacimiento: "))
#solicitamos la fecha actual al usuario
dia_actual = float(input("Ingrese el día de la fecha actual: "))
mes_actual = float(input("Ingrese el mes de la fecha actual: "))
anio_actual = float(input("Ingrese el año de la fecha actual: "))

#determinamos cuantos años tendrá el usuario al momento de calcular
edad = anio_actual-anio
if mes<mes_actual: #comprobamos que su cumpleaños ya se haya concretado en el año actual
    print(f"Su edad es de: {edad-1}") #reducimos en 1 el año en caso de que aún no cumplió en el año actual
elif mes>=mes_actual and dia>dia_actual:
    print(f"Su edad es de: {edad-1}")
else:
    print(f"Su edad es de: {edad}")
