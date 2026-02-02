#Haz un programa para gestionar las notas de una clase de 10 alumnos de los cuales sabemos su nombre y la nota obtenida. El programa debe permitir:
#1. Introducir los datos de los alumnos por teclado.
#2. Dado un nombre de un alumno, buscarlo y modificar su nota, mostrando el resultado por
#pantalla (empleando búsqueda secuencial).
#3. Dado un nombre de un alumno, buscarlo y mostrar la información por pantalla (empleando búsqueda binaria).
#4. Realizar la media de todas las notas.
#5. Realizar la media de las notas superiores o iguales a 5.
#6. Realizar la ordenación de los alumnos por notas en orden descendente y mostrar la nota del alumno con mejor nota.
#7. Realizar la ordenación de los alumnos por notas en orden ascendente y mostrar la nota del alumno que peor nota haya sacado.
alumnos = []
print("------ INTRODUCCIÓN DE DATOS ------")
for i in range(10):
    nombre = str(input(f"Nombre del alumno {i+1}: ")) #Nombre del alumno.
    nota = float(input(f"Nota de {nombre}: ")) #Nota del alumno.
    alumnos.append([nombre, nota])
#Función que sirve para modificar una nota
def modificar_nota(nombre_buscar, nueva_nota):
    for alumno in alumnos:
        if alumno[0].lower() == nombre_buscar.lower():
            alumno[1] = nueva_nota
            print(f"Nota modificada: {alumno[0]} ahora tiene {alumno[1]}")
            return
    print("El alumno no ha sido encontrado")
#Función que se usa para buscar una nota en función del nombre.
def busqueda_binaria(nombre_buscar):
    alumnos_ordenados = sorted(alumnos, key=lambda x: x[0].lower()) #Ordenar por nombre del alumno en vez de por la nota.
    inicio = 0
    fin = len(alumnos_ordenados) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        nombre_medio = alumnos_ordenados[medio][0].lower()
        if nombre_buscar.lower() == nombre_medio:
            print(f" Alumno encontrado: {alumnos_ordenados[medio]}")
            return
        elif nombre_buscar.lower() < nombre_medio:
            fin = medio - 1
        else:
            inicio = medio + 1
    print("El alumno no ha sido encontrado.")
#Función que saca la media total de las notas.
def media_total():
    return sum([al[1] for al in alumnos]) / len(alumnos)
#Función que enseña la media de aprobados.
def media_aprobados():
    aprobados = [al[1] for al in alumnos if al[1] >= 5]
    if len(aprobados) == 0:
        return 0
    return sum(aprobados) / len(aprobados)
#Función que ordena las notas en orden descendente y enseña la más alta.
def ordenar_descendente():
    ordenados = sorted(alumnos, key=lambda x: x[1], reverse=True)
    mejor = ordenados[0]
    print("\n--- Orden descendente (mejores primero) ---")
    for a in ordenados:
        print(a)
    print(f"La mejor nota es de {mejor[0]} con un {mejor[1]}.")
#Función que ordena las notas en orden ascendente y muestra la más baja.
def ordenar_ascendente():
    ordenados = sorted(alumnos, key=lambda x: x[1])
    peor = ordenados[0]
    print("\n--- Orden ascendente (peores primero) ---")
    for a in ordenados:
        print(a)
    print(f"La peor nota es de {peor[0]} con un {peor[1]}.")
print("\n----- GESTIÓN DE NOTAS -----")
while True:
    print("""
1. Modificar nota (búsqueda secuencial).
2. Buscar y mostrar alumno (búsqueda binaria).
3. Mostrar media total.
4. Mostrar media de aprobados (>=5).
5. Ordenar por notas DESC y mostrar mejor nota.
6. Ordenar por notas ASC y mostrar peor nota.
7. Salir.
""")
    opcion = input("Elige una opción de las ofrecidas arriba: ")
    if opcion == "1":
        nombre = input("Nombre del alumno: ")
        nueva = float(input("Nueva nota: "))
        modificar_nota(nombre, nueva)
    elif opcion == "2":
        nombre = input("Nombre del alumno: ")
        busqueda_binaria(nombre)
    elif opcion == "3":
        print(f"Media total: {media_total():.2f}")
    elif opcion == "4":
        print(f"Media de aprobados: {media_aprobados():.2f}")
    elif opcion == "5":
        ordenar_descendente()
    elif opcion == "6":
        ordenar_ascendente()
    elif opcion == "7":
        print("Salir de la gestión.")
        break
    else:
        print("Opción inválida.")