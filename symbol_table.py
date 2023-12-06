tabla = {}

resrvd = 0

def crea_variable(id, tipo):
    global resrvd
    add = resrvd
    correcto = True
    if id not in tabla:
        tabla[id] = (id, tipo, add)
        reserva_espacio(tipo)
    else:
        correcto = False
    return (correcto, resrvd - add)

def reserva_espacio(tipo):
    global resrvd
    if tipo == "char":
        resrvd += 1

    elif tipo == "int":
        resrvd += 4

    elif tipo == "float":
        resrvd += 4

    elif tipo == "string":
        resrvd += 8

    elif tipo == "bool":
        resrvd += 1
    