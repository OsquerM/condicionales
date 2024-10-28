#Crea un programa que simule una verificacion de contraseña. Pide al usuario que ingrese una contraseña y compara su entrada con una contraseña predefinida. Si coincide, muestra acceso concedido, de lo contrario, acceso denegado

password = input("Introduce la contraseña: ")

contrasenia = "oscarbenito"

if password == contrasenia:
    print("Acceso concedido")
else: 
    print("Acceso denegado")