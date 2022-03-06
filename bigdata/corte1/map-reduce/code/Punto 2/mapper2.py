                                                                                                 
import sys

precios=[]
ciudades = []
for line in sys.stdin:
        datos = line.split(",")
        precios.append(datos[1])
        ciudades.append(datos[6])

ciudades.pop(0)
precios.pop(0)

for i in range(len(ciudades)):
         ciudades[i]=ciudades[i].replace(" ", "")

for ciudad, precio in zip(ciudades,precios):
         print (str(ciudad)+"\t"+str(1)+"\t"+str(precio))