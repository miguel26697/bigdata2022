import sys

current_key = None
current_precio = []

for line in sys.stdin:
    precios, value, key, año = line.split("\t")
    value = int(value)
    precio = int(precio)
    current_precio.append(precio)
ordenados = sorted(current_precio)

for i in ordenados:
    print(str(key)+"\t"+str(año)+"\t"+str(i))
