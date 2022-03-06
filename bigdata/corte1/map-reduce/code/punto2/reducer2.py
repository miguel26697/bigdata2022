import sys

current_key = None
current_value = 0
current_precio = 0

for line in sys.stdin:
        key, value, precio = line.split("\t")
        value = int(value)
        precio = int(precio)
        if current_key == None:
                current_key = key
        if current_key == key:
                current_value += value
                current_precio += precio
        else:
                promedio = 0
                promedio = current_precio / current_value
                print (str(current_key) + "\t" + str(promedio))
                current_key = key
                current_value = value
                current_precio = precio
promedio = current_precio / current_value
print (str(current_key) + "\t" + str(promedio))