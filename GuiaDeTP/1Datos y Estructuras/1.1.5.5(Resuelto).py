
"""Se desea calcular el valor de la sección (S) de un conductor, la cual se determina en función de
la corriente eléctrica I y de la conductividad C del material (C=I/S). Además, a la sección así
obtenida se le incrementa un 25% por razones de seguridad."""


corriente = float(input("Ingrese el valor de la corriente electrica: "))
conductividad = float(input("Ingrese el valor de la conductividad del material: "))

print(f"El valor de la seccion del conductor es de {(corriente/conductividad)*1.25}")