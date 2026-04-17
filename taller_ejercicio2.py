print("CALCULADORA")

# funciones
def suma(a, b):
    c = a + b
    print("suma:", c)
    return c

def resta(a, b):
    c = a - b
    print("resta:", c)
    return c

def multi(a, b):
    c = a * b
    print("multiplicacion:", c)
    return c  

def divi(a, b):
    if b == 0:
        print("error: no se puede dividir entre 0")
        return
    c = a / b
    print("division:", c)
    return c

def potencia(base, exponente):
    """el prom requerido fue: 
    realiza en la calculadora una opcion para calcular la potencia
    la cual dependa de la funcion de multiplicacion

    por lo que toma el numero a como la base y el segundo como el exponente
    multiplicando por el numero b, n numero de veces la base hasta llegar al resultado
    de la potencia
    """
    resultado = 1
    for i in range(int(exponente)):
        resultado = multi(resultado, base)
    
    print("potencia:", resultado)
    return resultado

def factorial(n):
    """se utilizo el prom: en la calculadora crea una funcion
    factorial la cual dependa de la funcion multiplicacion

    el inicio del factorial siendo 1, en un rango de 1 hasta n+1
    multiplicando el resultado n veces necesarias
    """
    if n < 0:
        print("Error: no existe factorial de negativos")
        return
    
    resultado = 1
    for i in range(1, int(n) + 1):
        resultado = resultado * i
    
    print("factorial:", resultado)
    return resultado

def inversa(n):
    if n == 0:
        print("Error: no existe inversa")
        return
    
    resultado = 1 / n
    print("inversa:", resultado)
    return resultado

print("menu")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. potencia")
print("6. factorial")
print("7. inversa")

opcion = input("elige una opcion: ")

if opcion in ["1", "2", "3", "4", "5"]:
    a = float(input("numero a: "))
    b = float(input("numero b: "))
elif opcion in ["6", "7"]:
    a = float(input("numero a: "))
if opcion == "1":
    suma(a, b)
elif opcion == "2":
    resta(a, b)
elif opcion == "3":
    multi(a, b)
elif opcion == "4":
    divi(a, b)
elif opcion == "5":
    potencia(a, b)
elif opcion == "6":
    factorial(a)
elif opcion == "7":
    inversa(a)
else:
    print("opcion invalida")