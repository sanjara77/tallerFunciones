print("adivina el numero")
import random

def elegir_dificultad():
    """se creo una funcion para elegir la dificultad del juego
    y sus intentos
    """
    print("Selecciona dificultad:")
    print("1. facil (10 intentos)")
    print("2. medio (5 intentos)")
    print("3. dificil (3 intentos)")
    
    dificultad = input("elige una opción: ")
    
    if dificultad == "1":
        return 10
    elif dificultad == "2":
        return 5
    elif dificultad == "3":
        return 3

def generar_numero():
    """se llamo la biblioteca random.radint en un rango del 1 al 100 y se utilizo para la seleccion del numero secreto
    """
    return random.randint(1, 100)

def jugar(numero_secreto, intentos):
    """se utilizo el prom: para el codigo de generar numero realiza un juego de adivinar un numero del 1 al 100
    """
    while intentos > 0:
        print("intentos restantes:", intentos)
        
        intento = int(input("adivina el numero (1-100): "))
        
        if intento == numero_secreto:
            print("el numero es correcto")
            return
        
        elif intento < numero_secreto:
            print("el numero es mayor")
        
        else:
            print("el numero es menor")
        
        intentos -= 1
    
    print("el numero era:", numero_secreto)

intentos = elegir_dificultad()
numero = generar_numero()
jugar(numero, intentos)