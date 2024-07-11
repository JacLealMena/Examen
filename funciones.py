import os, msvcrt, csv, random



# Listas / Variables

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = []
num_min = 300000
num_max = 2500000

# Obligatorias

#LISTO
def asignar_sueldos_randoms():
    for n in trabajadores:
        sueldos.append(random.randint(num_min,num_max))
    print(">>> Sueldos ingresados con éxito!")
    esperar_tecla()

#LISTO pero Feo
def clasificar_sueldos():
    if len(sueldos) == 0:
        print(">>> No hay trabajadores ingresados!")
        esperar_tecla()
    else:
        total_sueldos = sum(sueldos)
        total_1 = 0
        total_2 = 0
        total_3 = 0
        for p in range(10):
            if sueldos[p] < 800000:
                L_sueldo_1 = f_sueldo_1()
                if L_sueldo_1[1] == 0:
                    total_1 =+ 0
                else:
                    total_1 =+ 1

            elif sueldos[p] >= 800000 and sueldos[p] <= 2000000:
                L_sueldo_2 = f_sueldo_2()
                if L_sueldo_2[1] == 0:
                    total_2 =+ 0
                else:
                    total_2 =+ 1

            else:
                total_3 = 0
                L_sueldo_3 = f_sueldo_3()
                if L_sueldo_3[1] == 0:
                    total_3 =+ 0
                else:
                    total_3 =+ 1      

        print(f"Sueldos menores a $800.000 TOTAL: {total_1}")
        print("Nombre empleado - Sueldo")
        for t in range(total_1):
            print({L_sueldo_1[0]},{L_sueldo_1[1]})
        
        print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {total_2}")
        print("Nombre empleado - Sueldo")
        for t in range(total_2):
            print({L_sueldo_2[0]}, {L_sueldo_2[1]})

        print(f"Sueldos superiores a $2.000.000 TOTAL: {total_3}")
        print ("Nombre empleado - Sueldo")
        for t in range(total_3):
            print({L_sueldo_3[0]}, {L_sueldo_3[1]})

        print(f"TOTAL SUELDOS: ${total_sueldos}")
        esperar_tecla()

#LISTO pero todo junto
def ver_estadisticas():
    if len(sueldos) == 0:
        print(">>> No hay sueldos ingresados!")
        esperar_tecla()
    else:
        sueldo_mas_bajo = min(sueldos)
        sueldo_mas_alto = max(sueldos)
        promedio_sueldos = sum(sueldos)/len(sueldos)
        multiplicacion = sueldos[0] * sueldos[1] * sueldos[2] * sueldos[3] * sueldos[4] * sueldos[5] * sueldos[6] * sueldos[7] * sueldos[8] * sueldos[9]
        media_geometrica = multiplicacion ** (1/len(sueldos))
        print(f"""
        * Sueldo más alto: ${sueldo_mas_alto}
        * Sueldo más bajo: ${sueldo_mas_bajo}
        * Promedio de sueldos: {promedio_sueldos}
        * Media geométrica: {media_geometrica}
                """)
        esperar_tecla()

# LISTO pero FEO
def reporte_sueldos():
    if len(sueldos) == 0:
        print(">>> No hay sueldos ingresados!")
        esperar_tecla()
    else:
        for s in range(10):
            indice = sueldos.index(sueldos[s])
            trabajadores_sueldo = [trabajadores[indice],sueldos[indice],[sueldos[indice]*0.07],[sueldos[indice]*0.12],[sueldos[indice]-((sueldos[indice]*0.07)+(sueldos[indice]*0.12))]]

        print("""
                Nombre del Empleado    Sueldo Base    Descuento Salud    Descuento AFP    Sueldo Líquido
            """)
        for s in range(10):
            indice = sueldos.index(sueldos[s])
            print(f"""
                {trabajadores[indice]}{""*15}{sueldos[indice]}{""*15}{sueldos[indice]*0.07}{""*15}{sueldos[indice]*0.12}{""*15}{(sueldos[indice])-((sueldos[indice]*0.07)+(sueldos[indice]*0.12))}
                """)
        with open("sueldos_trabajadores.csv","a+",newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(trabajadores_sueldo)
        
        esperar_tecla()
        
#LISTO
def salir_del_programa():
    limpiar()
    print(">>> Finalizando Programa...")
    print("Desarrollado por Jacquelinne Leal")
    print("RUT 21.583.380-1")
    exit()


# Utilidades

def limpiar():
    os.system('cls')

def esperar_tecla():
    print(">>> Presione una tecla para continuar...")
    msvcrt.getch()

#Funciones De Sueldo OPC 2

def f_sueldo_1():
    L_sueldo_1 = []
    try:
        indice = sueldos.index(sueldos[p])
        L_sueldo_1.append([trabajadores[indice],sueldos[indice]])
    except:
        L_sueldo_1 = ["---",0]
    return L_sueldo_1

def f_sueldo_2():
    L_sueldo_2 = []
    try:
        indice = sueldos.index(sueldos[p])
        L_sueldo_2.append([trabajadores[indice],sueldos[indice]])
    except:
        L_sueldo_2 = ["---",0]
    return L_sueldo_2

def f_sueldo_3():
    L_sueldo_3 = []
    try:
        indice = sueldos.index(sueldos[p])
        L_sueldo_3.append([trabajadores[indice],sueldos[indice]])
    except:
        L_sueldo_3 = ["---",0]
        return L_sueldo_3
    