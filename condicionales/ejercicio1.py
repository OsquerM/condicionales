# Ejercicio 1: Número Par o Impar
# Enunciado: Escribe un programa en Python que solicite al usuario un número entero. El programa debe determinar si el número es par o impar y mostrar el resultado en pantalla utilizando una estructura if-else. Asegúrate de usar la función input() para la lectura del número y int() para convertirlo a entero. Utiliza f-strings para mostrar el resultado.

num = int(input("Introduce un numero: "))

if num%2 == 0:
    print(f"El numero {num} es par")
else: 
    print(f"El numero {num} es impar")