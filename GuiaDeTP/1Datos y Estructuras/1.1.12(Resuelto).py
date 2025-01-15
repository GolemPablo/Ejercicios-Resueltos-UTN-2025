
"""Escriba un algoritmo que acepte un número entero mayor a 100 y menor a 1000, y muestre como está
compuesto (unidades, decenas y centenas) y si es múltiplo de 3 (Recordar: todo número cuya suma de
sus dígitos sea múltiplo de 3, lo es también)."""

#solicitamos al usuario la cantidad segun el rango de la consigna
num = int(input("Ingrese un número entero mayor a 100 y menor a 1000: "))
while num>=1000 or num<=100: #en caso de no cumplir con el rango, solicitarlo nuevamente hasta coincidir
    num = int(input("Incorrecto, por favor ingrese un número entero mayor a 100 y menor a 1000: "))

#calculamos si el numero ingresado es multiplo de 3 e imprimimos
if (num%3)==0:
    print(f"El número ingresado es multiplo de 3")
else:
    print(f"El número ingresado no es multiplo de 3")

#comprobamos cuantas unidades de cada tipo se necesitan para componer el número
if num >= 100:
    centenas = num // 100
    print(f"El número ingresado está compuesto por {centenas} unidades de 100")
    num %= 100 #tomamos el resto del numero en cada caso ya que en este caso, unidades de 100 ya no las necesitamos
#calculamos en decenas
if num >= 10:
    decenas = num // 10
    print(f"{decenas} unidades de 10")
    num %= 10
#calculamos en unidades
if num > 0:
    print(f"{num} unidades de 1")

#en caso de no poseer alguna unidad, el algoritmo no lo imprime