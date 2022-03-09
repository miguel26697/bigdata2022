import sys


for line in sys.stdin:
    datos = line.split(",")
    precios = None
    fechas = None
    if datos[1] != "Price":
        precios = datos[1]
    if datos[2] != "Date of Transfer":
        fechas = datos[2]
    
    if precios != None  and fechas != None:
        años = fechas.split("-")
        print(str(años[0]) + "\t" + str(años[1]) + "\t" + str(precios))

