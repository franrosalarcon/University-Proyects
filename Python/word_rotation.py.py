#Escriba un programa en Python que pida al usuario una frase, un número menor que el
# número de palabras de la frase, izquierda o derecha. No hay que hacer comprobaciones. El programa
# devuelve la misma frase, pero rotando cada una de las palabras en la frase el número de posiciones
# indicado. La rotación será a la derecha si el usuario introdujo derecha, e izquierda si introdujo izquierda.
# Hacerlo con funciones

def rotar_frase(frase, n,direccion):
    palabras = frase.split() # Convertimos la frase en una lista de palabras

    if direccion.lower() == "izquierda":
        resultado = palabras[n:] + palabras[:n] #[n:] toma desde el indice n hasta el final y [:n] toma desde el inicio hasta el indice n
    else:
        resultado = palabras[-n:] + palabras[:-n] #[-n:] toma las ultimas n palabras y [:-n] toma todas menos las ultimas n

    return " ".join(resultado) #Unimos la lista

def ejecutar_programa():
    frase = input("Introduce una frase: ")
    n = int(input("Introduce un número menor que el número de palabras: "))
    direccion = input("Introduce la dirección (izquierda/derecha): ")

    frase_final = rotar_frase(frase, n, direccion)
    print(f"Frase rotada: {frase_final}")

ejecutar_programa()

#FRANCISCO ROS ALARCÓN