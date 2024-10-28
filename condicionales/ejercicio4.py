#Pide al usuario que introduzca dos numeros enteros. Después, utiliza el if-else para comparar ambos números y mostrar un mensaje indicando cual es mayor o si son iguales.

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1 > num2:
    print(f"El numero {num1} es mayor que el {num2}")
else: 
    print(f"El {num2} es mayor que el {num1}")