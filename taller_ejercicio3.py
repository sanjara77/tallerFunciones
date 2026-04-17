print("inventario")

inventario = {
    "leche": {"cantidad": 6, "precio": 1000},
    "arroz": {"cantidad": 2, "precio": 2700},
    "coca-cola": {"cantidad": 8, "precio": 6000},
    "fresa": {"cantidad": 20, "precio": 200}
}

def mostrar_inventario(inventario):
    """se utilizo el prom:
    crea una funcion que se llame mostrar_inventario para que se muestre los productos
    que existen en el diccionario: inventario
    """
    if not inventario:
        print("inventario vacío")
        return
    
    print("inventario actualizado:")
    for producto in inventario:
        print(f"{producto} -> cantidad: {inventario[producto]['cantidad']}, Precio: {inventario[producto]['precio']}")


def agregar_producto(inventario, nombre, cantidad, precio):
    inventario[nombre] = {"cantidad": cantidad, "precio": precio}
    print(f"producto '{nombre}' agregado/actualizado")
    mostrar_inventario(inventario)


def eliminar_producto(inventario, nombre):
    if nombre in inventario:
        del inventario[nombre]
        print(f"producto '{nombre}' eliminado")
    else:
        print("el producto no existe")
    
    mostrar_inventario(inventario)


def valor_total(inventario):
    """se utilizo el prom:
    crea una funcion llamada valor_total la cual permita ver la suma de todos los
    valores de los productos del inventario
    """
    total = 0
    for producto in inventario:
        total += inventario[producto]["cantidad"] * inventario[producto]["precio"]
    
    print("valor total del inventario:", total)
    mostrar_inventario(inventario)

print("menu")
print("1. agregar producto")
print("2. eliminar producto")
print("3. mostrar inventario")
print("4. valor total")

opcion = input("elige una opción: ")

if opcion == "1":
    nombre = input("nombre del producto: ")
    cantidad = int(input("cantidad: "))
    precio = float(input("precio: "))
    agregar_producto(inventario, nombre, cantidad, precio)

elif opcion == "2":
    nombre = input("nombre del producto a eliminar: ")
    eliminar_producto(inventario, nombre)

elif opcion == "3":
    mostrar_inventario(inventario)

elif opcion == "4":
    valor_total(inventario)

else:
    print("Opción no válida")