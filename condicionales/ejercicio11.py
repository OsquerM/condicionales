# Objetivo: Simular el cálculo de impuestos en una tienda web, con distintas reglas fiscales
# según la ubicación del usuario.
# Pide al usuario que introduzca el precio de un producto y su país de residencia. Luego,
# calcula el precio final aplicando el impuesto correspondiente:
# ● Si el país es España, añade un 21% de IVA.
# ● Si el país es Francia, añade un 20% de IVA.
# ● Si el país es EEUU, no se añade ningún impuesto.
# ● Si el país es otro, muestra "País no admitido.

precio = float(input("Introduce un precio: "))
pais = input("Introduce el pais: ")

if pais == "españa":
    iva = precio*21/100
    resultado = iva + precio
    print(f"El precio final con impuestos es: {resultado}")
elif pais == "francia":
    iva = precio*20/100
    resultado = iva + precio
    print(f"El precio final con impuestos es: {resultado}")
elif pais == "eeuu":
    print(f"El precio final con impuestos es: {precio}")
else:
    print("Pais no admitido")