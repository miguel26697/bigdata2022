import sys

current_key = None
current_precio = []

for line in sys.stdin:
        key, value, precio, año = line.split("\t")
        value = int(value)
        precio = int(precio)
        print (str(key) + "\t" + str(precio) + "\t" + str(año))

