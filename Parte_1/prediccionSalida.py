def calcular(nums):
    total = 0
    for i, n in enumerate(nums):
        if i % 2 == 0:
            total += n
        else:
            total -= n
    return total
print(calcular([5, 3, 8, 2]))


"""
0+5-3+8-2 = 8
si la posición(i) es par. entonces se suma sino entonces se resta.
Si bien el cero para algunas personas no se considera par, el mod de 2
igual a cero se emplea para hacer referencia a par.  
Desde las propiedaddes matematicas el cero dividido cualquier numero es cero y mod tambein
"""