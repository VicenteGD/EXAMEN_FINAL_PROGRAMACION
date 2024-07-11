import os,time, random, csv
from funciones_p_f import *

os.system("cls")

while True:
    print("""MENÚ DE TRABAJADORES:
    1. ASIGNR SUELDOS ALEATORIOS 
    2. CLASIFICAR SUELDOS
    3. VER ESTADISTICAS
    4. REPORTE DE SUELDOS
    5. SALIR DEL PROGRAMA""")
    while True:
           
            try:
                opc=int(input("ingrese una opción (1,2,3,4,5): "))
                if opc in (1,2,3,4,5):
                    break
                else:
                    print("ERROR INGRESE UNA OPCIÓN VALIDA (1,2,3,4,5)")
            except:
                print("ERROR! ingrese un número entero!")
                os.system("cls")
    if opc==1:
        asignar_sueldos_aleatorios()
    elif opc==2:
        clasificar_sueldos()
    elif opc==3:
        ver_estadisticas()
    elif opc==4:
        reporte_de_sueldos()
    elif opc==5:
        salir_del_programa()
    else:
        print("ERROR! DEBE INGRESAR UNA OPCIÓN EXISTENTE (1,2,3,4,5)!")
    time.sleep(2)

