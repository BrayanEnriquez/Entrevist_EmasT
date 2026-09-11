def misterio(texto):
    resultado = ""
    for c in texto:
        if c not in resultado:
            resultado += c
    return resultado

"""
a. Retorna un texto con todas las letras distintas de un string
b. ban
c. Puede ser en un clave donde no se quiere que se repitan caracteres

"""