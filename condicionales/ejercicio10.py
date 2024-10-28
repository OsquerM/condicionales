# Pide al usuario que ingrese una dirección de correo electrónico. Luego, valida que el correo
# contenga un "@" y un "." en las posiciones correctas:
# ● Si ambos caracteres están presentes en los lugares apropiados, muestra "Correo
# válido."
# ● Si falta alguno de los caracteres o están en posiciones incorrectas, muestra "Correo
# inválido."

direccionCorreo = input("Introduce tu correo electronico: ")

if "@" in direccionCorreo and "." in direccionCorreo:
    posicionArroba = direccionCorreo.find("@")
    posicionPunto = direccionCorreo.find(".")
    if posicionArroba < posicionPunto:
        print("Correo valido")
    else:
        print("Correo invalido")
else:   
    print("Correo invalido")