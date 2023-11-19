
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

    #---------------SAM-----metodo para buscar expresion en estructura de datos
def variable_expr_ast(name,named_values):
     # Intenta obtener el valor asociado con el nombre de la variable
    if name in named_values:
        return named_values[name]
    else:
        log_error("Unknown variable name")

def log_error(message):
    # Implementa la lógica para manejar errores (puede imprimir un mensaje, lanzar una excepción, etc.).
    print(f"Error: {message}")
    return None

#  Ejemplo de uso:
# named_values = {"x": 33, "y": 10}
# result = variable_expr_astT("x", named_values)
# print(result)  # Esto imprimirá 33 si "x" está en named_values

# Ejemplo de función para representar llamadas a funciones
def call_expr(callee, args):
    # Busca la función en el diccionario
    callee_function = functions.get(callee)
    if not callee_function:
        return log_error("Unknown function referenced")

    # Verifica la cantidad correcta de argumentos
    if len(callee_function) != len(args):
        return log_error("Incorrect # arguments passed")

    # Simula la creación de la instrucción de llamada a función
    return f"Call {callee} with arguments: {args}"

# Diccionario para almacenar funciones
functions = {
    "add": ["a", "b"],
    "subtract": ["x", "y"]
}

# Ejemplo de uso
#result = call_expr("add", ["2", "3"])
#print(result)

