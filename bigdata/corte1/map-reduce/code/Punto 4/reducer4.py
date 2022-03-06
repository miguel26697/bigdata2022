import sys

current_key = None
current_precio = []

for line in sys.stdin:
        key, value, precio, año = line.split("\t")
        value = int(value)
        precio = int(precio)
        current_precio.append(precio)
ordenados = sorted(current_precio)
print (str(key) + "\t" + str(año) + "\t" + str(ordenados))