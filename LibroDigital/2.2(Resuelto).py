
"""Realizar un algoritmo que pida un valor entero que equivale a un número de pesos y me calcule a
cuantos billetes de 5000, 1000, monedas de 200, 25, 1."""

#solicitamos al usuario la cantidad de pesos a calcular
pesos = float(input("Ingrese una cantidad de pesos: "))

#comparamos en cada caso la cantidad de billetes/monedas para cada unidad
if pesos>=5000:
    print(f"La cantidad ingresada equivale a {pesos//5000} {'billete' if pesos==5000 else 'billetes'} de $5000")
    pesos %= 5000 #guardamos el resto ya que terminamos de calcular este billete y necesitamos pasar al siguiente de menor denominacion
if pesos>=1000:
    print(f"{pesos//1000} {'billete' if pesos==1000 else 'billetes'} de $1000")
    pesos %= 1000
if pesos>=200:
    print(f"{pesos//200} {'moneda' if pesos==200 else 'monedas'} de $200")
    pesos %= 200
if pesos>=25:
    print(f"{pesos//25} {'moneda' if pesos==25 else 'monedas'} de $25")
    pesos %= 25
if pesos>0:
    print(f"{pesos} {'moneda' if pesos==1 else 'monedas'} de $1")
    
#en caso de no poseer alguna unidad, el algoritmo no lo imprime