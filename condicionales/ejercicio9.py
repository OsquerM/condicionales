# Pide al usuario que introduzca su edad y si es miembro de un club (sí/no). Ofrece un
# descuento basado en las siguientes reglas:
# ● Si la persona tiene más de 65 años o es miembro del club, obtiene un 20% de
# descuento.
# ● Si tiene entre 18 y 65 años y no es miembro del club, obtiene un 10% de descuento.
# ● Si es menor de 18 años, obtiene un 15% de descuento.
# Muestra el porcentaje de descuento que le corresponde.

edad = int(input("Introduce tu edad: "))

miembro = input("¿Eres miembro del club?: (si/no): ")

if edad > 65 or miembro == "si":
    print("Obtiene un 20% de descuento")
elif edad >= 18 and edad <= 65 and miembro == "no":
    print("Obtienes un 10% de descuento")
elif edad < 18:
    print("Obtienes un 15% de descuento")
else:
    print("No te corresponde descuento")