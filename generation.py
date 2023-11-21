from llvmlite import ir
from llvmlite import binding as llvm



# BSS = []

# TEXT = []

# def define(var):
#     global BSS
#     BSS.append(var)

# def code(instruction):
#     global TEXT
#     TEXT.append(instruction)

# def generar_codigo():
#     global BSS, TEXT
#     codigo = "SECTION .bss\n"
#     for data in BSS:
#         codigo += f"\t{data}\n"
#     codigo += "SECTION .text\n"
#     for data in TEXT:
#         codigo += f"\t{data}\n"

#     with open("programa.asm",'w+') as f:
#         f.write(codigo)
#         f.close()

#     #---------------SAM-----metodo para buscar expresion en estructura de datos
# def variable_expr_ast(name,named_values):
#      # Intenta obtener el valor asociado con el nombre de la variable
#     if name in named_values:
#         return named_values[name]
#     else:
#         log_error("Unknown variable name")

# def log_error(message):
#     # Implementa la lógica para manejar errores (puede imprimir un mensaje, lanzar una excepción, etc.).
#     print(f"Error: {message}")
#     return None

# #  Ejemplo de uso:
# # named_values = {"x": 33, "y": 10}
# # result = variable_expr_astT("x", named_values)
# # print(result)  # Esto imprimirá 33 si "x" está en named_values

# # Ejemplo de función para representar llamadas a funciones
# def call_expr(callee, args):
#     # Busca la función en el diccionario
#     callee_function = functions.get(callee)
#     if not callee_function:
#         return log_error("Unknown function referenced")

#     # Verifica la cantidad correcta de argumentos
#     if len(callee_function) != len(args):
#         return log_error("Incorrect # arguments passed")

#     # Simula la creación de la instrucción de llamada a función
#     return f"Call {callee} with arguments: {args}"

# # Diccionario para almacenar funciones
# functions = {
#     "add": ["a", "b"],
#     "subtract": ["x", "y"]
# }

# # Ejemplo de uso
# #result = call_expr("add", ["2", "3"])
# #print(result)


# # Ejemplo de función para representar restas
# def resta(operaciones):
#     for izquierda, derecha in operaciones:
#         print("Esto es una resta de", izquierda, "-", derecha)

# Ejemplo de uso
#operaciones_resta = [(1, 2), (1, 3), (5, 2)]
#resta(operaciones_resta)


# metodo para For
# Crear un módulo de LLVM




class SimpleLoop:
    def __init__(self):
        # Crear un módulo de LLVM
        self.mi_modulo = ir.Module()

        # Crear una función llamada "bucle_simple"
        self.bucle_simple_func = ir.Function(self.mi_modulo, ir.FunctionType(ir.VoidType(), []), name="bucle_simple")

        # Crear bloques básicos
        self.entry_block = self.bucle_simple_func.append_basic_block(name="entry")
        self.after_block = self.bucle_simple_func.append_basic_block(name="after")

        # Declarar la función puts en el módulo
        puts_ty = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], False)
        self.puts_func = ir.Function(self.mi_modulo, puts_ty, name="puts")

    def for_code_ir(self):
        # Crear un constructor de IR
        builder = ir.IRBuilder(self.entry_block)

        # Inicializar el contador a 0
        contador = builder.alloca(ir.IntType(32), name="contador")
        builder.store(ir.Constant(ir.IntType(32), 0), contador)

        # Etiqueta del bucle
        etiqueta_bucle = self.bucle_simple_func.append_basic_block(name="bucle")
        builder.branch(etiqueta_bucle)
        builder.position_at_end(etiqueta_bucle)

        # Obtener el valor actual del contador
        valor_contador = builder.load(contador, name="valor_contador")

        # Realizar una comparación (por ejemplo, contador < 10)
        condicion = builder.icmp_signed("<", valor_contador, ir.Constant(ir.IntType(32), 10), name="condicion")

        # Crear bloques para el cuerpo del bucle y la salida del bucle
        cuerpo_bloque = self.bucle_simple_func.append_basic_block(name="cuerpo")
        salida_bloque = self.bucle_simple_func.append_basic_block(name="salida")

        # Hacer una rama condicional
        builder.cbranch(condicion, cuerpo_bloque, salida_bloque)

        # Posicionarse en el bloque del cuerpo del bucle
        builder.position_at_end(cuerpo_bloque)

        # Aquí deberías generar el código IR para el cuerpo del bucle
        # En este ejemplo, simplemente imprimimos el valor del contador usando puts
        format_str = ir.ArrayType(ir.IntType(8), 4)
        global_format_str = ir.GlobalVariable(self.mi_modulo, format_str, "format_str")
        global_format_str.initializer = ir.Constant(format_str, [ir.IntType(8)(char) for char in b"4%d\0"])
        format_str_ptr = builder.bitcast(global_format_str, ir.IntType(8).as_pointer())
        builder.call(self.puts_func, [format_str_ptr, valor_contador])

        # Incrementar el contador
        nuevo_valor_contador = builder.add(valor_contador, ir.Constant(ir.IntType(32), 1), name="nuevo_valor_contador")
        builder.store(nuevo_valor_contador, contador)

        # Hacer un salto incondicional al bloque del bucle
        builder.branch(etiqueta_bucle)

        # Posicionarse en el bloque de salida del bucle
        builder.position_at_end(salida_bloque)

        # Retornar desde la función
        builder.ret_void()

        # Imprimir el código IR generado de manera legible
        print(self.mi_modulo)
# Ejemplo de uso
simple_loop = SimpleLoop()
simple_loop.for_code_ir()
print(simple_loop.mi_modulo)
print("SI COMPILAAA")