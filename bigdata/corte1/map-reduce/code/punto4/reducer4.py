import sys

current_precios = []


for line in sys.stdin:
    precios, value, key, año = line.split("\t")
    value = int(value)
    precios = int(precios)
    current_precios.append(precios)

for i in sorted(current_precios):
    print(str(i)+"\t"+str(key)+"\t"+str(año))
