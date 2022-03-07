import sys


for line in sys.stdin:
        datos = line.split(",")
        precios = None
        ciudades = None
        if datos[1] != "Price":
                precios = datos[1]
        if datos[6] != "Town/City":
                ciudades = datos[6]

        if precios != None and ciudades != None:
                print (str(ciudades)+"\t"+str(1)+"\t"+str(precios))
