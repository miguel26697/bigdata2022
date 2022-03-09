import sys


for line in sys.stdin:
        datos = line.split(",")
        precios = None
        ciudades = None
        fechas = None
        if datos[1] != "Price":
                precios = datos[1]
        if datos[6] != "Town/City":
                ciudades = datos[6]
        if datos[2] != "Date of Transfer":
                fechas = datos[2]

        if precios != None and ciudades != None and fechas != None:
                años = fechas.split("-")
                if años [0] == "2015" and ciudades == "STAMFORD":
                 print (str(ciudades) + "\t"+ str(1) + "\t" + str(precios) + "\t" + str(años[0]))
