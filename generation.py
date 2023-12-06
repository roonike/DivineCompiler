from llvmlite import ir
from llvmlite import binding as llvm
from llvmlite import ir, binding
import ctypes

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

#     #---------------SAM-----metodo para buscar expresion en estructura de datos
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
# result = variable_expr_ast("x", named_values)
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

# # Diccionario para almacenar funciones
functions = {
    "add": ["a", "b"],
    "subtract": ["x", "y"]
}

# # Ejemplo de uso
# result = call_expr("add", ["2", "3"])
# print(result)


# Ejemplo de función para representar restas
def resta(operaciones):
    for izquierda, derecha in operaciones:
        print("Esto es una resta de", izquierda, "-", derecha)

# Ejemplo de uso
# operaciones_resta = [(1, 2), (1, 3), (5, 2)]
# resta(operaciones_resta)


# metodo para For
# Crear un módulo de LLVM


def for_code_ir():
      #Create an LLVM module
        miModulo = ir.Module()

        # Create a function  "simple_loop"
        bucleSimpleFunction = ir.Function(miModulo, ir.FunctionType(ir.IntType(32), []), name="bucleSimple")

        # Create basic blocks
        entryBlock = bucleSimpleFunction.append_basic_block(name="entry")
        bodyBlock = bucleSimpleFunction.append_basic_block(name="body")
        afterBlock = bucleSimpleFunction.append_basic_block(name="after")

        # Declare the puts function in the module
        putsTy = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], False)
        putsFunc = ir.Function(miModulo, putsTy, name="puts")

        # Start construction of IR
        builder = ir.IRBuilder(entryBlock)

        # Insert a conditional jump to the body block
        conditional = builder.icmp_unsigned('==', ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), 0))
        builder.cbranch(conditional, bodyBlock, afterBlock)

        # Build the loop bodyBuild the loop body
        builder.position_at_end(bodyBlock)

        # Call the puts function within the loop
        #builder.call(putsFunc, [ir.Constant(ir.IntType(8).as_pointer(), "Hola Mundo!\0")])

        # jump to start the loop
        builder.branch(entryBlock)

        # build block after loop
        builder.position_at_end(afterBlock)
        result = builder.add(ir.Constant(ir.IntType(32), 10), ir.Constant(ir.IntType(32), 32))
        builder.ret(result)
        # Print the Intermediate Representation (IR) Code
        print(str(miModulo))

# Llamar al método for
for_code_ir()

def create_equality_function(module):
    # Crear una función llamada "equality_function"
    equality_func_type = ir.FunctionType(ir.IntType(1), [ir.IntType(32), ir.IntType(32)])
    equality_func = ir.Function(module, equality_func_type, name="equality_function")

    # Crear un constructor de IR para la función
    builder = ir.IRBuilder(ir.Block(equality_func, name="entry"))

    # Obtener los argumentos de la función
    arg1, arg2 = equality_func.args

    # Realizar la operación de igualdad (arg1 == arg2)
    result = builder.icmp_signed("==", arg1, arg2, name="result")

    # Retornar el resultado
    builder.ret(result)

    return equality_func


# Inicializar el motor de ejecución para la funcion de igualdad
binding.initialize()
binding.initialize_native_target()
binding.initialize_native_asmprinter()

# Crear un módulo LLVM para la funcion de igualdad
llvm_module = ir.Module()

# Declarar la función de igualdad
equality_func_ty = ir.FunctionType(ir.IntType(1), [ir.IntType(32), ir.IntType(32)])
equality_func = ir.Function(llvm_module, equality_func_ty, name="equality_function")

# Crear el cuerpo de la función de igualdad
entry_block = equality_func.append_basic_block(name="entry")
builder = ir.IRBuilder(entry_block)

# Comparar los dos valores de entrada
param1, param2 = equality_func.args
result = builder.icmp_signed("==", param1, param2, name="result")

# Retornar el resultado
builder.ret(result)

# Imprimir el código IR generado
print("Código IR generado:")
print(str(llvm_module))

# Configurar el motor de ejecución MCJIT
target = binding.Target.from_default_triple()
target_machine = target.create_target_machine()
backing_mod = binding.parse_assembly(str(llvm_module))
engine = binding.create_mcjit_compiler(backing_mod, target_machine)

# Obtener el puntero a la función de igualdad generada
equality_func_ptr = engine.get_function_address("equality_function")

# Definir el tipo de la función ctypes correctamente
equality_function_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Convertir el puntero a la función LLVM a una función ctypes
equality_function = equality_function_type(equality_func_ptr)

# Llamar a la función de igualdad
result = equality_function(10, 10)
#print("Resultado de la igualdad:", result)