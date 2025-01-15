
"""Dado un año ingresado por el usuario, emitir el mensaje 'ACTUAL' si corresponde al año en curso,
'PASADO' si es menor y 'FUTURO' si es mayor."""

#utilizamos una funcion para importar la fecha actual del sistema
from datetime import datetime
anio_actual = datetime.now().year

#solicitamos al usuario el año a comparar
anio_ingresado = float(input("Ingrese un año: "))

#realizamos la comparacion e imprimimos
if anio_ingresado==anio_actual:
    print("ACTUAL")
elif anio_ingresado>anio_actual:
    print("FUTURO")
else:
    print("PASADO")
