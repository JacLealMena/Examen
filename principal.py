from funciones import *

while True:
    limpiar()
    print("""
        Menú
        1. Asignar sueldos aleatorios
        2. Clasificar sueldos
        3. Ver estadísticas.
        4. Reporte de sueldos
        5. Salir del programa
          """)
    opc = input("Opción > ")
    if opc == "1":
        asignar_sueldos_randoms()
    elif opc == "2":
        clasificar_sueldos()
    elif opc == "3":
        ver_estadisticas()
    elif opc == "4":
        reporte_sueldos()
    elif opc == "5":
        salir_del_programa()
    else:
        print(">>> OPCIÓN INVÁLIDA! Debe ingresar un número del menú")