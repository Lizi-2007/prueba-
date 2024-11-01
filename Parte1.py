nombre=input("Es un gusto saludarle estudiante, por favor ingrese su nombre")
print(nombre, "Ya que hemos realizado tres examenes por favor vaya ingresando su nota por cada uno de ellos")
nota_1=int(input("Ingrese la nota del primer examen"))
nota_2=int(input("Ingrese la nota del segundo examen"))
nota_3=int(input("Ingrese la nota del tercer examen"))
suma=nota_1+nota_2+nota_3
promedio=suma/3
print("su promedio es de ",promedio)
if promedio>=70:
    print("Aprobado")
elif promedio<70 and promedio>=60:
    print("Tiene que ir a ampliacion")
elif promedio<60:
    print("Reprobo")