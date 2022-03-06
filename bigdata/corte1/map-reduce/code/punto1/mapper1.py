import sys


for line in sys.stdin:
        datos = line.split(",")
        fechas = None
        if datos[2] != "Date of Transfer": 
                fechas = datos[2]
        if fechas != None:
         años = fechas.split("-")
         print (str(años[0]) + "\t" + str(1))
