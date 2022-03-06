import sys

condados = []
ciudades = []
for line in sys.stdin:
    datos = line.split(",")
    condados.append(datos[8])
    ciudades.append(datos[6])

ciudades.pop(0)
condados.pop(0)

for i in range(len(ciudades)):
    ciudades[i] = ciudades[i].replace(" ", "")

for i in range(len(condados)):
    condados[i] = condados[i].replace(" ", "")


for condado, ciudad in zip(condados, ciudades):
    print(str(condado) + "\t" + str(ciudad) + "\t" + str(1))
