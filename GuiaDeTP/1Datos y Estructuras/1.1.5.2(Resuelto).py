
"""Las raíces de una ecuación de segundo grado ax^2 + bx + c = 0 son reales si y sólo si el
discriminante dado por (b2 − 4ac) no es negativo. Se desea leer el valor de los coeficientes a, b,
c e imprimir el resultado del discriminante."""

#pedimos los coeficientes al usuario
a = float(input("Ingrese el coeficiente de A: "))
b = float(input("Ingresa el coeficiente de B: "))
c = float(input("Ingresa el coeficiente de C: "))

#realizamos el calculo para el discriminante
discriminante = b*2 - 4*a*c

print(f"El resultado del discriminante es: {discriminante}.")

#comprobamos si las raices son reales con el resultado del discriminante
if discriminante >= 0:
    print("Las raices son reales.")
else:
    print("Las raices no son reales.")
