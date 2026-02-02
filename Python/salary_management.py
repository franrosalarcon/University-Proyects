#Suponga una lista de la forma [(string, float)] que representa los nombres y sueldos de
#trabajadores de una empresa, donde el sueldo es un valor entre 0 y 2000€.

#1. Codifique un procedimiento que tome una lista como esa e incremente a cada trabajador su
#   sueldo hasta el mínimo interprofesional si este no llega al salario mínimo (actualmente
#   900€), indicando por pantalla a qué trabajador(es) se le(s) ha sido corregido su sueldo.

#2. Codifique y aplique una función que incremente el sueldo un 3% a todos los trabajadores
#   que están por debajo de la media, indicando a qué trabajadores se les ha incrementado el
#   sueldo. Estos trabajadores se deben mostrar en orden alfabético de nombre.

#3. Un programa probador que realice llamadas a estas funciones/procedimientos.


def ajustarminimo(trabajadores, minimo=900):
    print("Si ajustamos los sueldos al salario mínimo") #Procedimiento que ajusta los sueldos al salario mínimo si son inferiores. Modifica la lista directamente.
    # Recorremos la lista con enumerate para poder modificar elementos por índice
    for i, (nombre, sueldo) in enumerate(trabajadores):
        # Comprobamos si el sueldo actual es menor que el mínimo
        if sueldo < minimo:
            # Mostramos por pantalla qué trabajador se corrige y de cuánto a cuánto
            print(f" → Se corrige el sueldo de {nombre}: {sueldo}€ → {minimo}€")
            # Reemplazamos la tupla en la lista por una nueva con el sueldo actualizado
            trabajadores[i] = (nombre, minimo)
    print()

def incrementarbajomedia(trabajadores): #    Incrementa el 3% a los trabajadores con sueldo bajo la media. Devuelve una nueva lista (sin modificar la original) y muestra por pantalla los trabajadores afectados en orden alfabético.
    # Calcular salario medio
    media = sum(sueldo for _, sueldo in trabajadores) / len(trabajadores)
    print(f"Salario medio: {media:.2f}€") # Imprimimos la media con 2 decimales para que quede claro.

    # Crear nueva lista con incrementos
    nueva_lista = [] # nueva_lista guardará las tuplas (nombre, sueldo) resultantes (no tocamos la original)
    modificados = [] # modificados almacenará solo los nombres de los trabajadores que reciben el 3%

    for nombre, sueldo in trabajadores:
        # Comprobamos si el sueldo está por debajo de la media
        if sueldo < media:
            # Calculamos el nuevo sueldo aplicando un incremento del 3%
            # nuevo_sueldo = sueldo * 1.03
            nuevo_sueldo = sueldo * 1.03  # incremento del 3%
            # Añadimos la tupla actualizada a la nueva lista
            nueva_lista.append((nombre, nuevo_sueldo))
            # Registramos el nombre en la lista de modificados para mostrarlo después
            modificados.append(nombre)
        else:
            # Si no se aplica incremento, simplemente copiamos la tupla tal cual
            nueva_lista.append((nombre, sueldo))

    # Mostrar trabajadores afectados en orden alfabético
    if modificados:
        # Ordenamos alfabéticamente los nombres antes de mostrarlos
        print("== Trabajadores con incremento del 3% (ordenados alfabéticamente) ==")
        for nombre in sorted(modificados): #Gracias a sorted se ordena alfabéticamente
            print(f" → {nombre}")
    else:
        # Caso en que nadie está por debajo de la media
        print("Ningún trabajador está por debajo de la media.")

    print()
    return nueva_lista


def pedirtrabajadores():
    """
    Pide al usuario cuántos trabajadores quiere introducir
    y luego solicita nombre y sueldo de cada uno.
    Devuelve una lista de tuplas (nombre, sueldo).
    """
    trabajadores = []

    numero = int(input("¿Cuántos trabajadores quieres introducir? "))

    # Recorremos un bucle tantas veces como trabajadores quiera introducir el usuario
    for i in range(numero):
        # Indicamos el número de trabajador que estamos registrando (1, 2, 3...)
        print(f"\nTrabajador {i+1}:")
        # Pedimos el nombre del trabajador (string)
        nombre = input("  Nombre: ")
        # Pedimos el sueldo del trabajador y lo convertimos a float
        sueldo = float(input("  Sueldo: "))
        # Añadimos la tupla (nombre, sueldo) a la lista de trabajadores
        trabajadores.append((nombre, sueldo))
    #Mostramos por pantalla la lista completa introducida por el usuario
    print("\nTrabajadores introducidos:")
    print(trabajadores)
    print()
    return trabajadores

def general():

    # Lista inicial de ejemplo
    trabajadores = pedirtrabajadores()
    # Mostramos la lista original para comparar cambios posteriores
    print("Lista original:")
    print(trabajadores, "\n")

    # Ajuste al mínimo
    ajustarminimo(trabajadores)
    print("Tras ajustar al mínimo:")
    print(trabajadores, "\n")

    # Incremento del 3% a quienes estén por debajo de la media
    trabajadores = incrementarbajomedia(trabajadores)
    print("Tras incrementar sueldos bajos:")
    print(trabajadores, "\n")

general()
