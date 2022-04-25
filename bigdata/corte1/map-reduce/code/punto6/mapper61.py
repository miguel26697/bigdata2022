import sys

for line in sys.stdin:
    condado, value = line.split("\t" , 1 )
    value = int(value)
    print(str(value)+"\t"+ str(1))
