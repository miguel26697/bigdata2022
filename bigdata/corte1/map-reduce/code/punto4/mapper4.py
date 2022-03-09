import sys


for line in sys.stdin:
        datos = line.split(",")
        precios = None
        ciudades = None
        fechas = None
        
        if datos[6] != "Town/City":
                ciudades = datos[6]
        if datos[2] != "Date of Transfer":
                fechas = datos[2]

        if ciudades != None and fechas != None:
                años = fechas.split("-")
                if años [0] == "2015" and ciudades == "STAMFORD":
                        if datos[1] != "Price":
                                precios = datos[1]
                                print (str(precios) + "\t"+ str(1) + "\t" + str(ciudades) + "\t" + str(años[0]))
