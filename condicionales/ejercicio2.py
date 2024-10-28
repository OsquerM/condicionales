# Ejercicio 2: Calificación.
# Enunciado: Crea un programa en Python que pida al usuario su calificación en una escala de 0 a 10. El programa debe evaluar la calificación y mostrar un mensaje correspondiente según la siguiente escala:
# 9 a 10: Excelente
# 7 a 8.9: Buena
# 5 a 6.9: Aprobado
# 0 a 4.9: Reprobado

num = float(input("Introduce tu nota: "))

if num >= 9: 
    print(f"{num} Excelente")
elif num >= 7 and num <=8:
    print(f"Buena {num}")
elif num >= 5 and num <= 6.9:
    print(f"Aprobado {num}")
elif num >= 0 and num <= 4.9:
    print(f"Reprobado {num}")
else:
    print("Introduce un dato real")