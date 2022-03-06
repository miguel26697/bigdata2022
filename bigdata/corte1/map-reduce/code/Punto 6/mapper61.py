import sys

for line in sys.stdin:
    condado, value = line.split("\t")
    value = int(value)
    print(str(value)+"\t"+str(condado) + "\t" + str(1))
