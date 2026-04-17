print("analisis de temperatura")

temperaturas = [14,18,7,23,2,5,22,14,22,5,15,0,14,12,11,18,25,5,30,26,21,11,19,9]

def promedio(lista):
    suma = 0 #contador que permite realizar el promedio en la lista
    for i in lista:
        suma += i
    return suma / len(lista)#funcion para calcular el promedio (se le pregunto a la IA como se puede calcular el promedio de la lista)

resultado = promedio(temperaturas)# la IA agrego esta linea ya que no se mostraba el resultado de la funcion
print("Promedio:", resultado)


def maximo(temperatura):
    """se define una funcion maximo en la cual
    iniciando desde la posicion 0 de la lista comparando con un for
    si i la cual es una temperatura es mayor a la siguiente temperatura en la posicion de la lista
    """
    mayor = temperatura[0]
    for i in temperatura:
        if i > mayor:
            mayor = i
    
    print("Temperatura maxima:", mayor)
maximo(temperaturas) #con esto se llama a la funcion

def minimo(temperatura):
    menor = temperatura[0]
    for i in temperatura:
        if i < menor:
            menor = i
    
    print("Temperatura minima:", menor)
minimo(temperaturas)#con esto se llama a la funcion

def por_encima_del_promedio(temperatura, promedio):
    """el prom utilizado en la IA fue: crea en el codigo una funcion por_encima_del_promedio
    la cual calcule las temperaturas que estan por encima del promedio 
    """
    contador = 0
    for i in temperatura:
        if i > promedio:
            contador += 1
    
    print("Cantidad por encima del promedio:", contador)

por_encima_del_promedio(temperaturas, resultado) #con esto se llama a la funcion