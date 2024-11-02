
def adivina_el_numero():
    numero_secreto = 33
    
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    
    intento = int(input(f"Hola {nombre} {apellido}. ingrese un numero para intentar adivinar el numero secreto: "))
    
    if intento == numero_secreto:
        print(f"¡Felicidades {nombre} {apellido}! Has acertado el numero secreto, que es el {numero_secreto}. ")
    else:
        print(f"Gracias por participar, {nombre} {apellido}. El numero ingresado no es el correcto.")
    
adivina_el_numero()