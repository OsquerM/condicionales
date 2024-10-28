#Solicita al usuario su edad y muestra un mensaje en funcion del rango en el que se encuentre

edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad")
elif edad >= 18 and edad <= 65:
    print("Eres adulto")
elif edad > 65:
    print("Estas en la tercera edad")
else:
    print("Introduce un dato real")