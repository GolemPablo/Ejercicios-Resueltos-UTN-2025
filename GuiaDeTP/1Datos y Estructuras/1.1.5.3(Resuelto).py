
"""Se desea comprar una PC y una impresora. Calcular el precio total: el cual está dado por la suma
de los precios de costos, los porcentajes de ganancia del vendedor y un 21% de IVA. Supóngase una
ganancia del vendedor del 12% por la PC y 7% por la impresora. Se leen los costos y se imprimen el
precio total de ventas."""


costo_pc = int(input("Ingrese el costo de fabricación de la PC: "))
costo_impresora = int(input("Ingrese el costo de fabricación de la impresora: "))
ganancia_pc = int(input("Ingrese el porcentaje de ganancia por la venta de la PC: %"))
ganancia_impresora = int(input("y de la impresora: %"))
precio_total_de_venta = (costo_pc*(1+ganancia_pc/100)+costo_impresora*(1+ganancia_impresora/100))*1.21
print(f"El precio total por la venta de la PC y la impresora es de ${precio_total_de_venta}")