print("notas finales")

notas = {
    "Harry": [3.8, 4.0, 4.2],
    "Ron": [3.2, 3.8, 2.8],
    "Hermione": [5.0, 5.0, 5.0],
    "Draco": [4.5, 4.2, 5.0],
    "Nevil": [2.5, 3.0, 3.2]
}

def promedio_simple(notas):
    print("promedio simple")
    for estudiante in notas:
        promedio = sum(notas[estudiante]) / 3 #se suman todas las notas entre los [] de cada estudiante dividiendose entre 3 para sacar su promedio
        print(estudiante, ":", promedio)

def promedio_ponderado(notas):
    """se utilizo el prom:
    crea una funcion para calcular el promedio ponderado de los estudiantes en el diccionario notas
    """
    print("promedio ponderado")
    for estudiante in notas:
        n1, n2, n3 = notas[estudiante]
        promedio = n1*0.3 + n2*0.3 + n3*0.4 #se multiplican teniendo en cuenta el porcentaje de la nota
        print(estudiante, ":", promedio)

def mayor_promedio(notas):
    print("mejor estudiante")
    mejor = "" #guarda el nombre del estudiante
    mejor_prom = 0 #guarda el promedio
    
    for estudiante in notas: #se calcula el promedio ponderado 
        n1, n2, n3 = notas[estudiante]
        prom = n1*0.3 + n2*0.3 + n3*0.4
        
        if prom > mejor_prom: #se comparan promedios para determinar el mayot promedio
            mejor_prom = prom
            mejor = estudiante
    
    print(mejor, ":", mejor_prom)

def aprobados(notas):
    print("aprobados")
    for estudiante in notas:
        n1, n2, n3 = notas[estudiante]
        prom = n1*0.3 + n2*0.3 + n3*0.4
        
        if prom >= 3.0:
            print(estudiante, ":", prom)
        

def reprobados(notas):
    print("reprobados")
    for estudiante in notas:
        n1, n2, n3 = notas[estudiante]
        prom = n1*0.3 + n2*0.3 + n3*0.4
        
        if prom < 3.0:
            print(estudiante, ":", prom)

promedio_simple(notas)
promedio_ponderado(notas)
mayor_promedio(notas)
aprobados(notas)
reprobados(notas)
