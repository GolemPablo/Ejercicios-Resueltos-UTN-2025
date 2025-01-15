
"""Una persona decide realizar un viaje a Europa, para lo cual necesita una determinada cantidad de
euros. La persona tiene ahorrada una cierta suma en dólares y desea saber si es suficiente y, en
caso de haber diferencia (de más o de menos) a cuantos pesos equivale. Realice un algoritmo que
solucione el problema, para lo cual deberá prever que se ingresen las equivalencias de monedas que
considere necesarias (por ejemplo la cotizacion en pesos de dólar y/o del euro, o a cuantos euros
equivale un dólar)."""

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
