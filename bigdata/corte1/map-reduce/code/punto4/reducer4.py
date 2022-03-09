import sys

current_key = None


for line in sys.stdin:
    precios, value, key, año = line.split("\t")
    value = int(value)
    precio = int(precio)
    print(str("STAMFORD")+"\t"+str("2015")+"\t"+str(precio))


