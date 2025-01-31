"""Pagina: https://aed-frre.github.io/practica/1.1/

#EJERCICIO 0.1.5.0.1-------------------------------------------

marca = input("Ingrese la marca del automovil: ")
modelo = input("Ingrese el modelo del automovil: ")
print(f"Usted ingreso el automovil de modelo {modelo} de la marca {marca}")


#EJERCICIO 0.1.5.0.2----------------------------------------------

dolar_precio_en_pesos = float(input("Ingrese el valor del dolar en pesos al momento en el que realiza la conversion: "))
cantidad_dolar = float(input("Ingrese la cantidad de dolares que desea convertir: "))

print(f"La cantidad de {cantidad_dolar}USD convertidos a pesos da un valor de: ${dolar_precio_en_pesos*cantidad_dolar}")


#EJERCICIO 1.1.5.1---------------------------------------------

anio_actual = float(input("Ingrese el año actual: "))
anio_a_calcular = float(input("Ingrese el año para el cual quiere calcular: "))
precio_articulo = float(input("Ingrese el precio artículo: "))

#calculamos la cantidad de años que van a transcurrir
anios_transcurridos = anio_a_calcular-anio_actual

#le sumamos la tasa de inflacion y lo mostramos por pantalla
print(f"Considerando la tasa de inflacion anual del 4%, dentro de {anios_transcurridos} años, el precio del articulo va a ser de ${precio_articulo*(1.04**anios_transcurridos)}")


#EJERCICIO 1.1.5.2---------------------------------------------
 
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


#EJERCICIO 1.1.5.3---------------------------------------------

#solicitamos datos de costos y ganancias para los articulos
costo_pc = int(input("Ingrese el costo de fabricación de la PC: "))
costo_impresora = int(input("Ingrese el costo de fabricación de la impresora: "))
ganancia_pc = int(input("Ingrese el porcentaje de ganancia por la venta de la PC: %"))
ganancia_impresora = int(input("y de la impresora: %"))

#realizamos el calculo para determinar el precio final de los articulos e implimimos
precio_total_de_venta = (costo_pc*(1+ganancia_pc/100)+costo_impresora*(1+ganancia_impresora/100))*1.21
print(f"El precio total por la venta de la PC y la impresora es de ${precio_total_de_venta}")


#EJERCICIO 1.1.5.4---------------------------------------------

#solicitamos los datos del trapecio (dato de color: tambien pedimos el sistema de unidad)
base_1 = float(input("Ingrese el valor de la base inferior del trapecio: "))
base_2 = float(input("Ingrese el valor de la base superior del trapecio: "))
altura = float(input("Ingrese el valor de la altura de l trapecio: "))
medicion = input("Declara en que sistema de unidad están expresadas las medidas: ")

#calculamos la superficie e imprimimos
superficie = ((base_1+base_2)*altura)/2
print(f"La superficie del trapecio es de: {superficie} {medicion}")


#EJERCICIO 1.1.5.5---------------------------------------------

#solicitamos los valores de corriente y conductividad
corriente = float(input("Ingrese el valor de la corriente electrica: "))
conductividad = float(input("Ingrese el valor de la conductividad del material: "))

#imprimimos el resultado
print(f"El valor de la seccion del conductor es de {(corriente/conductividad)*1.25}")


#EJERCICIO 1.1.5.6---------------------------------------------

#solicitamos al usuario los datos del primer numero complejo
a = float(input("Ingrese la parte real del primer número compuesto: "))
b = float(input("Ingrese la parte imaginaria del primer número compuesto: "))
#solicitamos al usuario los datos del segundo numero complejo
c = float(input("Ingrese la parte real del segundo número compuesto: "))
d = float(input("Ingrese la parte imaginaria del segundo número compuesto: "))

#realizamos el calculo para ambas partes del numero complejo
parte_real = a*c-d*b
parte_imaginaria = a*d+b*c
#imprimimos
print(f"El producto entre los 2 numeros complejos es: ({parte_real},{parte_imaginaria})")


#EJERCICIO 1.1.5.7---------------------------------------------

#solicitamos las medidas al usuario
x = float(input("Ingrese el primer valor: "))
y = float(input("Ingrese el segundo valor: "))
z = float(input("Ingrese el tercer valor: "))

#emitimos los valores y el resultado del valor medio entre estos
print(f"El valor de X es: {x}, el valor de Y es: {y} y el valor de Z es: {z}.")
print(f"Su media aritmética es de:{(x+y+z)/3}")


#EJERCICIO 1.1.6---------------------------------------------

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


#EJERCICIO 1.1.7---------------------------------------------

#solicitamos los datos al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma = num1+num2

#según el valor, imprimimos el resultado según la consigna
if suma<=50:
    print("Suma <=50")
elif suma>50 and suma<=100:
    print("Suma > 50 y <= 100")
elif suma>100 and suma<=200:
    print("Suma > 100 y <= 200")
else:
    print("Suma > 200")


#EJERCICIO 1.1.8---------------------------------------------

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


#EJERCICIO 1.1.9---------------------------------------------

#solicitamos al usuario los datos necesarios para calcular
euro_necesita = float(input("Ingrese la cantidad de euros que necesita para su viaje: "))
dolar_ahorro = float(input("Ingrese la cantidad de dolares del que dispone actualmete: "))
valor_dolar = float(input("Ingrese en valor del dolar expresado en pesos: "))
valor_euro = float(input("Ingrese el valor del euro expresado en dolares: "))

#determinamos cuantos euros posee
euros = dolar_ahorro/valor_euro
if euros>euro_necesita: #comprobamos si tiene los necesarios y detependiendo del caso retornamos la diferencia
    pesos = ((euros-euro_necesita)*valor_euro)*valor_dolar
    print(f"Usted dispone de la cantidad necesaria de euros para realizar el viaje, con un exceso de ${pesos} pesos argentinos")
elif euros==euro_necesita:
    print=("Usted dispone de la cantidad justa de euros para realizar el viaje")
else:
    pesos =((euro_necesita-euros)*valor_euro)*valor_dolar
    print(f"Usted no dispone de la cantidad necesaria para realizar el viaje satisfactoriamente, le falta una suma de ${pesos} pesos argentinos")


#EJERCICIO 1.1.10---------------------------------------------

#solicitamos los datos
a = float(input("Ingrese un número entero llamado A: "))
b = float(input("Ingrese otro número entero llamado B: "))

#determinamos si ambos numeros son divisores
if ((a%b)==0):
    print("A es divisor de B")
elif ((b%a)==0):
    print("B es divisor de A")
else:
    print("A y B No son divisores")


#EJERCICIO 1.1.11---------------------------------------------

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


#EJERCICIO 1.1.12---------------------------------------------

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


#EJERCICIO 1.1.13---------------------------------------------

#solicitamos al usuario la cantidad de dinero que necesitamos calcular
pesos = int(input("Ingrese una cantidad de dinero mayor a $100 y menor a $1000: "))
while pesos >= 1000 or pesos <= 100: #comprobamos que el valor se encuentre delntro del rango, de lo contrario, solicitar de nuevo
    pesos = int(input("Incorrecto, por favor ingrese una cantidad de dinero mayor a $100 y menor a $1000: "))

#mismo caso del ejercicio 1.1.13
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

#incluimos la opcion de imprimir 'billete' o 'billetes' en caso de ser 1 o varios billetes

#EJERCICIO 1.1.14---------------------------------------------"""





"""#EJERCICIO 1.1.15---------------------------------------------

pisos = float(input("Ingrese la cantidad de pisos del edificio: "))
altura_p = float(input("Ingrese la altura promedio de los pisos del edificio: "))

print(f"La altura aproximada del edificio es de: {(pisos*altura_p)*3.28}")"""