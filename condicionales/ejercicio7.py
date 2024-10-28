# Pide al usuario que introduzca tres números. Luego, muestra un mensaje indicando si:

num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
num3 = int(input("Introduce el tercero numero: "))

if num1 == num2 == num3:
    print("Todos los numeros son iguales")
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("Todos los numeros son diferentes")
else:
    print("Solo dos de los numeros son iguales")
