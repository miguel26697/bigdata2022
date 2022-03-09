import sys

current_key = None
current_precio = []

for line in sys.stdin:
    precios, value, key, año = line.split("\t")
    value = int(value)
    precio = int(precio)
    current_precio.append(precio)


for i in sorted(current_precio):
    print(str("STAMFORD")+"\t"+str("2015")+"\t"+str(i))
