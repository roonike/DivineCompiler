from llvmlite import ir
from llvmlite import binding as llvm

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


# Ejemplo de función para representar restas
def resta(operaciones):
    for izquierda, derecha in operaciones:
        print("Esto es una resta de", izquierda, "-", derecha)

# Ejemplo de uso
#operaciones_resta = [(1, 2), (1, 3), (5, 2)]
#resta(operaciones_resta)


# metodo para For
# Crear un módulo de LLVM
mi_modulo = ir.Module()

# Crear una función llamada "bucle_simple"
bucle_simple_func = ir.Function(mi_modulo, ir.FunctionType(ir.VoidType(), []), name="bucle_simple")

# Crear un bloque de entrada para la función
entrada_bloque = bucle_simple_func.append_basic_block(name="entrada")
constructor = ir.IRBuilder(entrada_bloque)

# Inicializar el contador a 0
contador = constructor.alloca(ir.IntType(32), name="contador")
constructor.store(ir.Constant(ir.IntType(32), 0), contador)

# Etiqueta del bucle
etiqueta_bucle = bucle_simple_func.append_basic_block(name="bucle")
constructor.branch(etiqueta_bucle)
constructor.position_at_end(etiqueta_bucle)

# Obtener el valor actual del contador
valor_contador = constructor.load(contador, name="valor_contador")

# Realizar una comparación (por ejemplo, contador < 10)
condicion = constructor.icmp_signed("<", valor_contador, ir.Constant(ir.IntType(32), 10), name="condicion")

# Crear bloques para el cuerpo del bucle y la salida del bucle
cuerpo_bloque = bucle_simple_func.append_basic_block(name="cuerpo")
salida_bloque = bucle_simple_func.append_basic_block(name="salida")

# Hacer una rama condicional
constructor.cbranch(condicion, cuerpo_bloque, salida_bloque)

# Posicionarse en el bloque del cuerpo del bucle
constructor.position_at_end(cuerpo_bloque)

# Aquí deberías generar el código IR para el cuerpo del bucle
# En este ejemplo, simplemente imprimimos el valor del contador
constructor.call(ir.FunctionType(ir.VoidType(), [ir.IntType(32)]).as_pointer(), 
                  mi_modulo.get_global("printf"),
                  [ir.Constant(ir.ArrayType(ir.IntType(8), 4), b"%d\n"), valor_contador])

# Incrementar el contador
nuevo_valor_contador = constructor.add(valor_contador, ir.Constant(ir.IntType(32), 1), name="nuevo_valor_contador")
constructor.store(nuevo_valor_contador, contador)

# Hacer un salto incondicional al bloque del bucle
constructor.branch(etiqueta_bucle)

# Posicionarse en el bloque de salida del bucle
constructor.position_at_end(salida_bloque)

# Retornar desde la función
constructor.ret_void()

# Imprimir el código IR generado
print(mi_modulo)

#EJEMPLO DE USO
# Configurar el motor de ejecución
# llvm.initialize()
# llvm.initialize_native_target()
# llvm.initialize_native_asmprinter()

# # Crear un motor de ejecución
# target = llvm.Target.from_default_triple()
# target_machine = target.create_target_machine()
# execution_engine = llvm.create_mcjit_compiler(llvm.parse_assembly(str(mi_modulo)), target_machine)

# # Obtener una referencia a la función "bucle_simple"
# bucle_simple_func_ptr = execution_engine.get_function_address("bucle_simple")

# # Llamar a la función desde Python
# bucle_simple_func_ptr()

# # Limpiar y finalizar
# llvm.shutdown()