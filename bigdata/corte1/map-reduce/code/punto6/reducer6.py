import sys

current_key = None
current_value = 0
current_town = None

ciudades ={}
for line in sys.stdin:
        key, value = line.split("\t",1)
        ciudad, count = value.split(',',1)
        count = int(count)
        if key == current_key:
           if ciudad not in ciudades:
            ciudades[ciudad] = True
            current_value += count
        else:
          if current_key:
            print (str(current_key) + "\t" + str(current_value))
          current_key = key
          current_value = count
if key == current_key:
  print (str(current_key) + "\t" + str(current_value))