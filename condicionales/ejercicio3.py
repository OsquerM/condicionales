# Ejercicio 3: Cálculo del IMC.
# Enunciado: Desarrolla un programa en Python que calcule el Índice de Masa Corporal (IMC) de una persona. El programa debe solicitar al usuario su peso en kilogramos y su altura en metros. Luego, debe calcular el IMC usando la fórmula IMC = peso / (altura ** 2) y mostrar el resultado con dos decimales. Además, el programa debe clasificar el IMC en una de las siguientes categorías:
# Bajo de peso: IMC < 18.5
# Peso normal: 18.5 <= IMC < 24.9
# Sobrepeso: 25 <= IMC < 29.9
# Obesidad: IMC >= 30
# Utiliza una estructura if-elif-else para clasificar el IMC y f-strings para mostrar los resultados.

kg = float(input("Introduce tu peso: "))
altura = float(input("Introduce tu altura: "))

imc = (kg)/ (altura ** 2)

if imc < 18.5:
    print(f"Bajo de peso {imc:.2f}")
elif  18.5 <= imc < 24.9:
    print(f"Peso normal {imc:.2f}")
elif 25 <= imc < 29.9:
    print(f"Sobrepeso {imc:.2f}")
elif imc >= 30:
    print(f"Obesidad {imc:.2f}")
else:
    print("Introduce un dato real")
    