
BSS = []

TEXT = []

def define(var):
    global BSS
    BSS.append(var)

def code(instruction):
    global TEXT
    TEXT.append(instruction)

def generar_codigo():
    global BSS, TEXT
    codigo = "SECTION .bss\n"
    for data in BSS:
        codigo += f"\t{data}\n"
    codigo += "SECTION .text\n"
    for data in TEXT:
        codigo += f"\t{data}\n"

    with open("programa.asm",'w+') as f:
        f.write(codigo)
        f.close()