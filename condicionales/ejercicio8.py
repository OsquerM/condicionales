# Crea un programa que valide un nombre de usuario y una contraseña. Pide al usuario
# ambos datos y comprueba que:
# ● Si el nombre de usuario es "admin" y la contraseña es "1234", muestra "Acceso
# concedido."
# ● Si el nombre de usuario es incorrecto pero la contraseña es correcta, muestra
# "Usuario incorrecto."
# ● Si el nombre de usuario es correcto pero la contraseña es incorrecta, muestra
# "Contraseña incorrecta."
# ● Si ambos son incorrectos, muestra "Acceso denegado."


usuario = input("Introduce tu nombre de usuario: ")
contrasenia = (input("Introduce la contraseña: "))

nombre = "admin"
password = "123"

if usuario == nombre and contrasenia == password:
    print("Acceso concedido")
elif usuario != nombre:
    print("Usuario incorrecto")
elif contrasenia != password:
    print("Contraseña incorrecta")
else:
    print("Acceso denegado")