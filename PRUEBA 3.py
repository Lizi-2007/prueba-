edad = int(input("Introduce tu edad: "))

ingresos = float(input("Introduce tus ingresos mensuales en colones: "))

if edad > 18 and ingresos > 50000:
    print("Debes tributar.")
else:
    print("No debes tributar.")