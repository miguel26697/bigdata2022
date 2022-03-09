import sys

current_key = None

for line in sys.stdin:
        precio, value, key, año = line.split("\t")
        value = int(value)
        precio = int(precio)
        print (str(key) + "\t" + str(precio) + "\t" + str(año))

