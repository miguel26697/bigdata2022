import sys

fechas = []
for line in sys.stdin:
        datos = line.split(",")
        fechas.append(datos[2])

fechas.pop(0)

años = []
for date in fechas:
        dates = date.split("-")
        años.append(dates[0])

for año in años:
         print (str(año) + "\t" + str(1))