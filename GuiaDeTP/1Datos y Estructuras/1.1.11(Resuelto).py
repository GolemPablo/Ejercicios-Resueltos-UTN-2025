
"""Dado un año ingresado por el usuario, emitir el mensaje 'ACTUAL' si corresponde al año en curso,
'PASADO' si es menor y 'FUTURO' si es mayor."""


from datetime import datetime
anio_actual = datetime.now().year

anio_ingresado = float(input("Ingrese un año: "))

if anio_ingresado==anio_actual:
    print("ACTUAL")
elif anio_ingresado>anio_actual:
    print("FUTURO")
else:
    print("PASADO")
