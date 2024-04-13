# Reto #1: EL "LENGUAJE HACKER"

# * Escribe un programa que reciba un texto y transforme lenguaje natural a
# * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# *  se caracteriza por sustituir caracteres alfanuméricos.
# * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# *   con el alfabeto y los números en "leet".
# *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

import string

# Lista con abecedario
letras = list(string.ascii_lowercase)
# print(len(letras))

# Lista con equivalentes
equivalentes = ['4','I3','[',')','3','|=','&','#','1',',_|','>|','1','/\/\'','^/','0','|*','(_,)','I2','5','7','(_)','\/','\/\/','><','j','2']
# print(len(equivalentes))

# Diccionario letras + equivalentes leet
dicc_leet = dict(zip(letras,equivalentes))
# print(dicc_leet)

# Variable que almacena la palabra insertada por el usuario
texto = input('Introduzca el texto que quiere transformar a leet languaje: ').lower()


# Función de traducción
def leetTransform (frase):
    traduccion = '' # Variable traducción = ''
    for i in frase: # Iteración por cada letra de la palabra insertada por el usuario
        traduccion += dicc_leet[i] # Busca el equivalente de la letra dentro del diccionario y lo añade a la variable traducción
    return traduccion # retorna la variable traducción

print(leetTransform(texto)) # Llama la función de traducción usando como input la variable texto e imprime el resultado de la función