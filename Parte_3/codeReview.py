def actualizar_stock(inventario, movimientos):
    for nombre, cantidad in movimientos:
        inventario[nombre] += cantidad
    for nombre in inventario:
        if inventario[nombre] <= 0:
            del inventario[nombre]
    return inventario

"""
1 - Que pasa cuando normbre no exite en inventario? 
    if nombre in inventario:
        inventario[nombre] += cantidad
    else:
        return No existe {nombre} en el inventario

2 - Cantidad = int
    if nombre in inventario and type(cantidad) == int:
            inventario[nombre] += cantidad
        else:
            return No existe {nombre} en el inventario
3 - Que pasa cuando movimientos esta vacia. Validar
    if not movimientos:
        return




""":