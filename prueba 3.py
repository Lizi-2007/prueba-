num_examenes = int(input("Ingrese la cantidad de examenes realizados: "))
 
suma_notas = 0
 
for i in range(num_examenes):
     nota = int(input(f"Ingrese la nota del examen {1+1}: "))
     suma_notas += nota
     
promedio = suma_notas / num_examenes

print(f"La nota final es: {promedio:.2f}")

if promedio >= 70:
    print("El estudiante ha aprovado.")
elif 60 <= promedio < 70:
    print("El estudiante debe ir a ampliacion.")
else:
    print("El estudiante ha reprobado.")