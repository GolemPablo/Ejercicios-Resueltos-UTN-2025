
"""¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?"""


primos = []

for numero in range(1, 1001):
    if numero > 1:  # Los números menores o iguales a 1 no son primos
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(numero)

print(f"Números primos entre 1 y 1000: {primos}")
print(f"Cantidad de números primos: {len(primos)}")