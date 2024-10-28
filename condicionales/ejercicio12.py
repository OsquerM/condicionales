# Pide al usuario que ingrese una URL. Valida si:

# La URL comienza con "http://" o "https://".
# La URL contiene al menos un punto (".") después del dominio.
# Si ambas condiciones se cumplen, muestra "URL válida", de lo contrario, muestra "URL
# inválida."

# Solicitar al usuario que ingrese una URL
url = input("Ingrese una URL: ")

# Validar la URL
if (url.startswith("http://") or url.startswith("https://")) and (url.count(".") > 0):
    print("URL válida")
else:
    print("URL inválida")
