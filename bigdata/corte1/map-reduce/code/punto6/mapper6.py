import sys

condados = []
ciudades = []
for line in sys.stdin:
    datos = line.split(",")
    condados = None
    ciudades = None
    if datos[6] != "Town/City":
        ciudades = datos[6]
    if datos[8] != "County":
        condados = datos[8]
    if condados != None and ciudades != None:
        print(str(condados) + "\t" + str(ciudades) + "\t" + str(1))