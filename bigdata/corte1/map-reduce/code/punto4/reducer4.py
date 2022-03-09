import sys

current_key = None
cuurent_price = 0
for line in sys.stdin:
        precio, value, key, año = line.split("\t")
        value = int(value)
        precio = int(precio)
        print (str(precio) + "\t" + str(key) + "\t" + str(año))

