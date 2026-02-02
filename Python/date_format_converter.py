#a) Pida la fecha en formato: dd/mm/aa El usuario puede meter para día y mes menor que 10 las dos cifras o solo una (ver ejemplos)
#b) Devuelva la fecha en formato: dd de mes del año aaaa, dd es el día metido por el usuario, pero si menor que 10 no lleva el 0 delante (ver ejemplos) mes es el nombre del mes al que corresponde mm. aaaa es el aa completado con los dígitos 20 por delante

meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

while True:
    entrada = input("\nIntroduce la fecha en formato dd/mm/aa: ")

    try:
        #1. Comprobamos y verificamos que las tres partes introducidas tengan barras
        partes = entrada.split("/")
        if len(partes) != 3:
            print("Error: El formato es incorrecto. Debe usar dos barras (dd/mm/aa).")
            continue

        #2. Comprobamos y verificamos que las tres partes sean números
        if not(partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit()):
            print("Error: Los valores introducidos deben ser números enteros.")
            continue

        dia = int(partes[0])
        mes_num = int(partes[1])
        año = partes[2]

        #3. Comprobamos y verificamos el rango de los meses
        if mes_num < 1 or mes_num > 12:
            print(f"Error: El mes {mes_num} es erroneo (debe estar entre 1 y 12).")
            continue

        #4. Comprobamos y verificamos el rango de días
        if dia < 1 or dia > 31:
            print(f"Error: El día {dia} es erroneo (debe estar entre 1 y 31).")
            continue

        #5. Comprobamos y verificamos que el año introducido tenga 2 digitos
        if len(año) != 2:
            print("Error: El año debe tener exactamente dos dígitos")
            continue
        #Imprimimos el resultado una vez ya verificado
        nombre_mes = meses[mes_num - 1]
        print(f"Resultado: {dia} de {nombre_mes} del año 20{año}")

    except Exception as e:
        print(f"Error: {e}")

#FRANCISCO ROS ALARCÓN
