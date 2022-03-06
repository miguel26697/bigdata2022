import sys

precios=[]
ciudades = []
fechas = []
for line in sys.stdin:
        datos = line.split(",")
        precios.append(datos[1])
        ciudades.append(datos[6])
        fechas.append(datos[2])

ciudades.pop(0)
precios.pop(0)
fechas.pop(0)

años = []
for date in fechas:
        dates = date.split("-")
        años.append(dates[0])

for i in range(len(ciudades)):
         ciudades[i]=ciudades[i].replace(" ", "")

for ciudad, precio, año in zip(ciudades,precios,años):
         if año == "2015" and ciudad == "STAMFORD":
          print (str(ciudad) + "\t"+ str(1) + "\t" + str(precio) + "\t" + str(año))