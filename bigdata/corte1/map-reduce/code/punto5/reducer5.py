import sys

current_key = None
current_precio = 0
mes_actual = 0
current_value = 0
mayor = 0
mes_ganador = 0
for line in sys.stdin:
    año, mes, value = line.split("\t")
    value = int(value)
    if current_key == None:
        current_key = año
        mes_actual = mes

    if current_key == año:
        if mes_actual == mes:
            current_value += value
        else:
            mes_actual = mes
            current_value = value

        if mayor < current_value:
            mayor = current_value
            mes_ganador = mes

    else:
        print(str(current_key) + "\t" + str(mes_ganador) + "\t" + str(mayor))
        current_key = año
        mes_actual = mes
        current_value = value
        mayor = value
        mes_ganador = mes

print(str(current_key) + "\t" + str(mes_ganador) + "\t" + str(mayor))
