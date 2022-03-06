import sys

current_key = None
current_value = 0
current_precio = 0

for line in sys.stdin:
        key, value, precio = line.split(" ")
        value = int(value)
        precio = int(precio)
        if current_key == None:
                current_key = key
                current_precio = precio
        if current_key == key:
                current_value += value
                if current_precio > precio:
                  current_precio = precio
        else:
                print (str(current_key) + "\t" + str(current_precio))
                current_key = key
                current_value = value
                current_precio = precio

print (str(current_key) + "\t" + str(current_precio))