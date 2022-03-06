import sys

current_key = None
current_value = 0
current_cantidad = 0
for line in sys.stdin:
    cantidad, condado, value = line.split("\t")
    cantidad = int(cantidad)
    value = int(value)
    if current_key == None:
        current_key = value
        current_cantidad = cantidad
    if current_cantidad == cantidad:
        current_value += value
    else:
        print(str(current_value) + "\t" + str(current_cantidad))
        current_value = value
        current_cantidad = cantidad

print(str(current_value)+"\t"+str(current_cantidad))
