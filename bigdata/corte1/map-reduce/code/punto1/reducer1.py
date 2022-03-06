import sys

current_key = None
current_value = 0
for line in sys.stdin:
        line.strip()
        key, value = line.split("\t")
        value = int(value)
        if current_key == None:
                current_key = key
        if current_key == key:
                current_value += value
        else:
                print (str(current_key) + "\t" + str(current_value))
                current_key = key
                current_value = value
print (str(current_key) + "\t" + str(current_value))