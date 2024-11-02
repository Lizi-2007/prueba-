# Solicitar la edad del usuario
edad = int(input("Introduce tu edad: "))

# Determinar el costo según la edad
if edad <= 10:
    costo = 3000
elif edad < 15:
    costo = 5000
elif edad < 18:
    costo = 7500
else:
    costo = 10000

# Mostrar el costo a pagar
print(f"El costo de entrada es {costo} colones.")