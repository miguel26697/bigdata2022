import sys

current_key = None
current_value = 0
current_town = None
for line in sys.stdin:
        condado, ciudad, value = line.split("\t")
        value = int(value)
        if current_key == None:
          current_key = condado
          current_town = ciudad

        if current_key == condado:
          if current_town != ciudad:
              current_value += value

        else:
           print (str(current_key) + "\t" + str(current_value))

           current_key = condado
           current_value = value

print (str(current_key) + "\t" + str(current_value))