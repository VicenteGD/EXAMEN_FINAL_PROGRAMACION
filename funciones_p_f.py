import csv, random
#import random
#aleatorio=random.randint(menor,mayor)
trabajadores=["Juan Pérez", "María García", "Carlos López","Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
      "Isabel Gómez", "Francisco Díaz", "Elena Fernández" ]      
va_datos=[]
def asignar_sueldos_aleatorios():
    print("ASIGNAR SUELDOS ALEATORIOS ")
    aleatorio_1=random.randint(300000,2500000)
    aleatorio_2=random.randint(300000,2500000)
    aleatorio_3=random.randint(300000,2500000)
    aleatorio_4=random.randint(300000,2500000)
    aleatorio_5=random.randint(300000,2500000)
    aleatorio_6=random.randint(300000,2500000)
    aleatorio_7=random.randint(300000,2500000)
    aleatorio_8=random.randint(300000,2500000)
    aleatorio_9=random.randint(300000,2500000)
    aleatorio_10=random.randint(300000,2500000)

    #print(f"Juan Pérez     :${aleatorio_1}")
    #print(f"María García   :${aleatorio_2}")
    #print(f"Carlos López   :${aleatorio_3}")
    #print(f"Ana Martínez   :${aleatorio_4}")
    #print(f"Pedro Rodríguez:${aleatorio_5}")
    #print(f"Laura Hernández:${aleatorio_6}")
    #print(f"Miguel Sánchez :${aleatorio_7}")
    #print(f"Isabel Gómez   :${aleatorio_8}")
    #print(f"Francisco Díaz :${aleatorio_9}")
    #print(f"Elena Fernández:${aleatorio_10}")  
           
    #datos_sueldos=[f"Juan Pérez:${aleatorio_1}",f"\nMaría García:${aleatorio_2}",f"\nCarlos López:${aleatorio_3}",f"Ana Martínez   :${aleatorio_4}",f"Pedro Rodríguez:${aleatorio_5}",f"Laura Hernández:${aleatorio_6}",f"Miguel Sánchez :${aleatorio_7}",f"Isabel Gómez   :${aleatorio_8}",f"Francisco Díaz :${aleatorio_9}",f"Elena Fernández:${aleatorio_10}"]
    #print(datos_sueldos)

    valor_total=(aleatorio_1+aleatorio_2+aleatorio_3+aleatorio_4+aleatorio_5+aleatorio_6+aleatorio_7+aleatorio_8+aleatorio_9+aleatorio_10)
    print(f"VALOR TOTAL: {valor_total}")

def clasificar_sueldos(datos_sueldos):
  print("CLASIFICAR SUELDOS")
  if not trabajadores:
      print("no hay datos")
  else:
      print(datos_sueldos)
      
def ver_estadisticas(datos_sueldos):
    print("ESTADISTICAS: ")
    print("sueldos más bajo: ")
    print("sueldo más alto:")
    print("datos sueldos: ")
    print(datos_sueldos)

def reporte_de_sueldos(datos_sueldos):
    print (datos_sueldos)
    #trabajador0
    descuento_salud_0=((datos_sueldos[0])*0.07)
    descuento_afp_0=((datos_sueldos[0])*0.12)
    sueldo_liquido_0=((datos_sueldos[0])-descuento_salud_0-descuento_afp_0)
    #trabajador1
    descuento_salud_1=((datos_sueldos[1])*0.07)
    descuento_afp_1=((datos_sueldos[1])*0.12)
    sueldo_liquido_1=((datos_sueldos[1])-descuento_salud_1-descuento_afp_1)
    #trabajador2
    descuento_salud_2=((datos_sueldos[2])*0.07)
    descuento_afp_2=((datos_sueldos[2])*0.12)
    sueldo_liquido_2=((datos_sueldos[2])-descuento_salud_2-descuento_afp_2)
    #trabajador3
    descuento_salud_3=((datos_sueldos[3])*0.07)
    descuento_afp_3=((datos_sueldos[3])*0.12)
    sueldo_liquido_3=((datos_sueldos[3])-descuento_salud_3-descuento_afp_3)
    #trabajador4
    descuento_salud_4=((datos_sueldos[4])*0.07)
    descuento_afp_4=((datos_sueldos[4])*0.12)
    sueldo_liquido_4=((datos_sueldos[4])-descuento_salud_4-descuento_afp_4)
    #trabajador5
    descuento_salud_5=((datos_sueldos[5])*0.07)
    descuento_afp_5=((datos_sueldos[5])*0.12)
    sueldo_liquido_5=((datos_sueldos[5])-descuento_salud_5-descuento_afp_5)
    #trabajador6
    descuento_salud_6=((datos_sueldos[6])*0.07)
    descuento_afp_6=((datos_sueldos[6])*0.12)
    sueldo_liquido_6=((datos_sueldos[6])-descuento_salud_6-descuento_afp_6)
    #trabajador7
    descuento_salud_7=((datos_sueldos[7])*0.07)
    descuento_afp_7=((datos_sueldos[7])*0.12)
    sueldo_liquido_7=((datos_sueldos[7])-descuento_salud_7-descuento_afp_7)
    #trabajador8
    descuento_salud_8=((datos_sueldos[8])*0.07)
    descuento_afp_8=((datos_sueldos[8])*0.12)
    sueldo_liquido_8=((datos_sueldos[8])-descuento_salud_8-descuento_afp_8)  
    #trabajador9
    descuento_salud_9=((datos_sueldos[9])*0.07)
    descuento_afp_9=((datos_sueldos[9])*0.12)
    sueldo_liquido_9=((datos_sueldos[9])-descuento_salud_9-descuento_afp_9)

    print("REPORTE DE SUELDOS:")
    print("NOMBRE EMPLEADO:   SUELDO BASE:    DESCUENTO SALUD:   DESCUENTO AFP   SUELDO LÍQUIDO: ")
    print(f"Juan Pérez     :{datos_sueldos[0]}  {descuento_salud_0} {descuento_afp_0}  {sueldo_liquido_0} ")
    print(f"María García   :{datos_sueldos[1]}  {descuento_salud_1} {descuento_afp_1}  {sueldo_liquido_1} ")
    print(f"Carlos López   :{datos_sueldos[2]}  {descuento_salud_2} {descuento_afp_2}  {sueldo_liquido_2} ")
    print(f"Ana Martínez   :{datos_sueldos[3]}  {descuento_salud_3} {descuento_afp_3}  {sueldo_liquido_3} ")
    print(f"Pedro Rodríguez:{datos_sueldos[4]}  {descuento_salud_4} {descuento_afp_4}  {sueldo_liquido_4} ")
    print(f"Laura Hernández:{datos_sueldos[5]}  {descuento_salud_5} {descuento_afp_5}  {sueldo_liquido_5} ")
    print(f"Miguel Sánchez :{datos_sueldos[6]}  {descuento_salud_6} {descuento_afp_6}  {sueldo_liquido_6} ")
    print(f"Isabel Gómez   :{datos_sueldos[7]}  {descuento_salud_7} {descuento_afp_7}  {sueldo_liquido_7} ")
    print(f"juanito perez  :{datos_sueldos[8]}  {descuento_salud_8} {descuento_afp_8}  {sueldo_liquido_8} ")
    print(f"juanito perez  :{datos_sueldos[9]}  {descuento_salud_9} {descuento_afp_9}  {sueldo_liquido_9} ")

    nombre_Archivo=input("ingrese el nombre de su archivo")

    with open(nombre_Archivo +".csv", "x", newline="")as archivo:
        escritor=csv.writer(archivo)
        for vicho in trabajadores:
            print("REPORTE DE SUELDOS:")
        print("NOMBRE EMPLEADO:   SUELDO BASE:    DESCUENTO SALUD:   DESCUENTO AFP   SUELDO LÍQUIDO: ")
        print(f"Juan Pérez     :{datos_sueldos[0]}  {descuento_salud_0} {descuento_afp_0}  {sueldo_liquido_0} ")
        print(f"María García   :{datos_sueldos[1]}  {descuento_salud_1} {descuento_afp_1}  {sueldo_liquido_1} ")
        print(f"Carlos López   :{datos_sueldos[2]}  {descuento_salud_2} {descuento_afp_2}  {sueldo_liquido_2} ")
        print(f"Ana Martínez   :{datos_sueldos[3]}  {descuento_salud_3} {descuento_afp_3}  {sueldo_liquido_3} ")
        print(f"Pedro Rodríguez:{datos_sueldos[4]}  {descuento_salud_4} {descuento_afp_4}  {sueldo_liquido_4} ")
        print(f"Laura Hernández:{datos_sueldos[5]}  {descuento_salud_5} {descuento_afp_5}  {sueldo_liquido_5} ")
        print(f"Miguel Sánchez :{datos_sueldos[6]}  {descuento_salud_6} {descuento_afp_6}  {sueldo_liquido_6} ")
        print(f"Isabel Gómez   :{datos_sueldos[7]}  {descuento_salud_7} {descuento_afp_7}  {sueldo_liquido_7} ")
        print(f"juanito perez  :{datos_sueldos[8]}  {descuento_salud_8} {descuento_afp_8}  {sueldo_liquido_8} ")
        print(f"juanito perez  :{datos_sueldos[9]}  {descuento_salud_9} {descuento_afp_9}  {sueldo_liquido_9} ")
        escritor.writerow(vicho)
    
def salir_del_programa():
   print("Finalizando programa...")
   print("Desarrollado por: Vicente Garrido")
   print("Rut: 21.456.946-9")
   exit()
   

