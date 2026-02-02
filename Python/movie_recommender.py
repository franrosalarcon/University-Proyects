pelicula1 = "Bebe Jefazo"
pelicula2 = "Harry Potter"
pelicula3 = "El Correo"

while True:
    try:
        edad = int(input("Introduzca su edad: "))
        if 12>edad>0:
            print("La mejor pelicula para ti es",pelicula1)
            break
        elif 18>edad>=12:
            print("La mejor pelicula para ti es",pelicula2)
            print("Pero también puedes ver",pelicula1)
            break
        elif edad>=18:
            print("La mejor pelicula para ti es",pelicula3)
            print("Pero también puedes ver",pelicula2, "y", pelicula1)
            break
        else:
            print("La edad no es valida")
    except ValueError:
        print("Error! la edad introducida no es valida")

