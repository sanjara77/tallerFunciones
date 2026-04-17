print("maquina dispensadora")

def productos():
    """se le pidio a la IA realizar una maquina dispensadora 
    la cual tenga como funciones:

    productos
    mostrar_productos
    seleccionar_productos
    pagar
    resultado

    la maquina muestra los productos que tiene disponibles y sus precios
    permite seleccionar al usuario el producto que quiere mostrando luego
    un mensaje para ingresar el dinero, si el dinero no es suficiente
    se muestra el mensaje "dinero insuficiente" y si el monto excede el pedido
    se realiza el mensaje de devuelta restando el dinero recibido por el precio del producto

    """
    return {
        "agua": 2000,
        "coca-cola": 3000,
        "papas margarita": 2500,
        "chocolate": 1500,
        "oreo": 1800,
        "arroz con leche" : 5000
    }

def mostrar_productos(diccionario):
    print("productos disponibles:")
    for producto in diccionario:
        print(producto, ":", diccionario[producto]) #imprime cada producto y su precio

def seleccionar_producto(diccionario):
    eleccion = input("elige un producto: ")
    
    if eleccion in diccionario:
        return eleccion
    else:
        print("producto no disponible")
        return None #no se retorna ningun valor

def pagar(precio):
    dinero = int(input("ingresa plata: "))
    
    if dinero < precio:
        print("plata insuficiente")
        return None
    
    cambio = dinero - precio
    return cambio

def resultado(producto, cambio):
    if cambio is None:
        return
    
    print(f"has comprado {producto}")
    
    if cambio > 0:
        print("te devuelvo:", cambio)
    else:
        print("no hay cambion a dar")

productos = productos()
mostrar_productos(productos)
producto = seleccionar_producto(productos)

if producto is not None:
    precio = productos[producto]
    print("precio:", precio)
    
    cambio = pagar(precio)
    
    resultado(producto, cambio)