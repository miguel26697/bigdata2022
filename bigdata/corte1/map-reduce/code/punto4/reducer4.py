import sys

current_key = None


for line in sys.stdin:
    precios, value, key, año = line.split("\t")
    value = int(value)
    precio = int(precio)
    print(str(precio)+"\t"+str(key)+"\t"+str(año))
