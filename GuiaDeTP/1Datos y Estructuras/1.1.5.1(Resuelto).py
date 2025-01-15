
"""Escribir un programa que permita calcular el precio de un artículo para un año dado, considerando
que la inflación es del 4 por 100 anual."""

anio_actual = float(input("Ingrese el año actual: "))
anio_a_calcular = float(input("Ingrese el año para el cual quiere calcular: "))
precio_articulo = float(input("Ingrese el precio artículo: "))

#calculamos la cantidad de años que van a transcurrir
anios_transcurridos = anio_a_calcular-anio_actual

#le sumamos la tasa de inflacion y lo mostramos por pantalla
print(f"Considerando la tasa de inflacion anual del 4%, dentro de {anios_transcurridos} años, el precio del articulo va a ser de ${precio_articulo*(1.04**anios_transcurridos)}")
