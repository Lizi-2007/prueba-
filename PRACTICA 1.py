def calcularpaga(horas_trabajadas, coste_por_hora):
    paga = horas_trabajadas * coste_por_hora
    return paga

horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
coste_por_hora = float(input("Ingrese el coste por hora: "))

paga = calcularpaga(horas_trabajadas, coste_por_hora)
print(f"La paga correspondiente es: {paga:.2f} unidades monetarias.")