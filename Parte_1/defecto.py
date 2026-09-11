def promedio_positivos(nums):
    suma = 0
    conteo = 0
    for n in nums:
        if n > 0:
            suma += n
        conteo += 1
    return suma / conteo


"""
a. La suma esta bien porque esta dentro del if pero el conteo no
esta afuera no depende de la condicion de mayor que cero (positivos). 
Entonces cuenta cada numero asi sea negativo

b. 
if n > 0:
    suma += n
    conteo += 1

c. 1- Que nums este vacio
    if len(nums) < 0:
        return
    
    antes del for
    
    2- Que todos los numeros de nums sean menores que creo.

    despues del for

    if suma == 0 and conteo == 0:
        return

"""