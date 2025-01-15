
"""¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?"""

#creamos un conjunto para guardar los número primos
primos = []
#comprobamos 1 por 1 gracias a un for
for numero in range(1, 1001): #repetimos desde el 1 hasta que llegue a 1001
    if numero > 1:  # Los números menores o iguales a 1 no son primos, comprobamos que sea mayor ya que en el caso que sea 2, este si es primo
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1): #consideramos 'i' un selector que se mueve numero por numero para poder compararlo
            if numero % i == 0: #un numero primo solo es divisible entre él mismo y el uno, por ende, su resto no puede ser 0
                es_primo = False
                break
        if es_primo:
            primos.append(numero) #en caso de ser primero, guardamos uno por uno en el conjunto previamente creado

#imprimimos los resultados
print(f"Cantidad de números primos: {len(primos)}")
print(f"Números primos entre 1 y 1000: {primos}")