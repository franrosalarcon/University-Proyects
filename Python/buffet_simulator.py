comida = ["Hamburguesa", "Pizza", "Patatas"] #Lista con una serie de comidas
calorias = [500,350,200] #Lista con las calorias de cada comida
final = 0
seguir = "si"
print("BIENVENIDO AL BUFFET PAQUITA SALAS")
print("##################################\n"
      "P P P P P P     S S S S S S       \n"
      "P P P P P P P   S S S S S S S     \n"
      "P P       P P   S S S             \n"
      "P P P P P P P     S S S S S S     \n"
      "P P P P P P         S S S S S S   \n"
      "P P                       S S S   \n"
      "P P               S S S S S S     \n"
      "P P             S S S S S S       \n"
      "##################################")
while seguir == "si":
    if (final + calorias[0]) > 2000:
        print("Ya has comido demasiado")
        break
    final+=calorias[0]
    print(f"Se ha comido una {comida[0]} , Total: {final} calorias")
    seguir = input("¿Quiere seguir comiendo (si/no): ").lower()
    if seguir == "si":
        if (final + calorias[1]) > 2000:
            print("Ya has comido demasiado")
            break
        final+=calorias[1]
        print(f"Se ha comido una {comida[1]} , Total: {final} calorias")
        seguir = input("¿Quiere seguir comiendo (si/no): ").lower()
        if seguir == "si":
            if (final + calorias[2]) > 2000:
                print("Ya has comido demasiado")
                print("Hasta la proxima!")
                break
            final+=calorias[2]
            print(f"Se ha comido unas {comida[2]}, Total: {final} calorias")
            seguir = input("¿Quiere seguir comiendo (si/no): ").lower()
            if seguir == "si":
                continue
            elif seguir == "no":
                print("Hasta la proxima!")
                break
            else:
                print("Error!, caracteres introducidos invalidos")
                break
        elif seguir == "no":
            print("Hasta la proxima!")
            break
        else:
            print("Error!, caracteres introducidos invalidos")
            break
    elif seguir == "no":
        print("Hasta la proxima!")
        break
    else:
        print("Error!, caracteres introducidos invalidos")
        break