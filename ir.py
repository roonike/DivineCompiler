from llvmlite import ir
import llvmlite
import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int, c_float, c_bool, c_void_p, c_char_p,cast


llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

#impresion
def imprimir(module,func_name,r_type = c_void_p):
    llvm_ir_parsed = llvm.parse_assembly(str(module))
    llvm_ir_parsed.verify()

    # JIT
    target_machine = llvm.Target.from_default_triple().create_target_machine()
    engine = llvm.create_mcjit_compiler(llvm_ir_parsed, target_machine)
    engine.finalize_object()

    #Run the function with name func_name. This is why it makes sense to have a 'main' function that calls other functions.
    entry = engine.get_function_address(func_name)
    cfunc = CFUNCTYPE(r_type)(entry)
    
    result = cfunc()

    print('The llvm IR generated is:')
    print(module)
    print()
    if r_type == c_void_p:
        print('Function does not return a value.')
    elif r_type == c_char_p:
        result_str = cast(result, c_char_p).value.decode("utf-8")
        print(f'It returns "{result_str}"')
    else:
        print(f'It returns {result}')
    print()



#DECLARACIONES#

#enteros de 32 bits
def int_decl():
    i32 = ir.IntType(32)
    module = ir.Module(name="INT_Declaration")
    fnty = ir.FunctionType(ir.VoidType(),[])
    func_name = "int_decl"
    func = ir.Function(module,fnty,name= func_name)
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    builder.alloca(i32, name="intVar")
    builder.ret_void()
    imprimir(module,func.name,)

#Punto flotante de precision simple
def float_decl():
    f32 = ir.FloatType()
    module = ir.Module(name="Float_Declaration")
    fnty = ir.FunctionType(ir.VoidType(),[])
    func = ir.Function(module,fnty,name= "float_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    builder.alloca(f32, name="floatVar")
    builder.ret_void()
    imprimir(module,func.name)


#Que es un string, mas que un arreglo de chars
#Que es un char mas que un entero de 8 bits traducido
def string_decl():
    char = ir.IntType(8)
    string = ir.ArrayType(char,0)
    module = ir.Module(name="String_Declaration")
    fnty = ir.FunctionType(ir.VoidType(),[])
    func = ir.Function(module,fnty,name= "string_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    builder.alloca(string, name="stringVar")
    builder.ret_void()
    imprimir(module,func.name)

#Entero de 1 bit, 0 = false, 1 = true
def bool_decl():
    bool = ir.IntType(1)
    module = ir.Module(name="Bool_Declaration")
    fnty = ir.FunctionType(ir.VoidType(),[])
    func = ir.Function(module,fnty,name= "bool_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    builder.alloca(bool, name="boolVar")
    builder.ret_void()
    imprimir(module,func.name)


#Arreglo de 3x1
def array(val1,val2,val3,retval):
    i32 = ir.IntType(32)
    module = ir.Module(name="Array")
    ret_type = i32
    arg_type = list()
    fnty = ir.FunctionType(ret_type, arg_type)
    func = ir.Function(module, fnty, name="Array_example")
    block = func.append_basic_block('entry')
    builder = ir.IRBuilder(block)
    array_type = ir.ArrayType(i32,3)
    array_pointer = builder.alloca(array_type)
    
    i32_0 = ir.Constant(i32, 0)
    i32_1 = ir.Constant(i32, 1)
    i32_2 = ir.Constant(i32, 2)
    
    pointer_to_index_0 = builder.gep(array_pointer, [i32_0, i32_0]) #gets address of array[0]
    pointer_to_index_1 = builder.gep(array_pointer, [i32_0, i32_1]) #gets address of array[1]
    pointer_to_index_2 = builder.gep(array_pointer, [i32_0, i32_2]) #gets address of array[2]
    
    builder.store(i32(val1), pointer_to_index_0) # posicion 0 = val1
    builder.store(i32(val2), pointer_to_index_1) # posicion 1 = val2
    builder.store(i32(val3), pointer_to_index_2) #posicion 2 = val3
    if(retval == 0):
        value = builder.load(pointer_to_index_0)
    elif(retval == 1):
        value = builder.load(pointer_to_index_1)
    elif(retval == 2):
        value = builder.load(pointer_to_index_2)
    builder.ret(value)
    imprimir(module,func.name,c_int)
    
def decl():
    int_decl()
    float_decl()
    string_decl()
    bool_decl()

#ASIGNACIONES#

#Asignar valor a entero de 32 bits 
def int_asign(val):
    i32 = ir.IntType(32)
    module = ir.Module(name="INT_Asign")
    fnty = ir.FunctionType(i32,[])
    func = ir.Function(module,fnty,name= "int_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    int_var = builder.alloca(i32, name="intVar")
    int_val = i32(val)
    builder.store(int_val,int_var)
    builder.ret(int_val)
    imprimir(module,func.name,c_int)

#asignar valor a flotante
def float_asign(val):
    f32 = ir.FloatType()
    module = ir.Module(name="Float_Asign")
    fnty = ir.FunctionType(f32,[])
    func = ir.Function(module,fnty,name= "float_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    float_var = builder.alloca(f32, name="floatVar")
    float_val = f32(val)
    builder.store(float_val,float_var)
    builder.ret(float_val)
    imprimir(module,func.name,c_float)

#asignar valor a string
def string_asign(val):
    char = ir.IntType(8)
    string = ir.ArrayType(char, len(val))
    string_arg = [ord(value) for value in val]
    module = ir.Module(name="String_Asign")
    fnty = ir.FunctionType(ir.PointerType(char), [])
    func = ir.Function(module, fnty, name="string_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    string_var = builder.alloca(string, name="stringVar")
    string_val = string(string_arg)
    builder.store(string_val, string_var)
    builder.ret(string_var)
    print(module)

#asignar valor a bool
def bool_asign(val):
    bool = ir.IntType(1)
    module = ir.Module(name="Bool_Asign")
    fnty = ir.FunctionType(bool,[])
    func = ir.Function(module,fnty,name= "bool_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    bool_var = builder.alloca(bool, name="boolVar")
    bool_val = bool(val)
    builder.store(bool_val,bool_var)
    builder.ret(bool_val)
    imprimir(module,func.name,c_bool)

def asign():
    int_asign(1337)
    float_asign(42.1337)
    string_asign("Hola Mundo")
    bool_asign(True)



def ir_and(bool1,bool2):
    bool = ir.IntType(1)
    module = ir.Module(name="AND_example")
    fnty = ir.FunctionType(bool,(bool,bool))
    func = ir.Function(module,fnty,name="And")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    resul = builder.and_(bool(bool1),bool(bool2))
    builder.ret(resul)
    imprimir(module,func.name,c_bool)
    
def ir_or(bool1,bool2):
    bool = ir.IntType(1)
    module = ir.Module(name="OR_example")
    fnty = ir.FunctionType(bool,(bool,bool))
    func = ir.Function(module,fnty,name="OR")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    resul = builder.or_(bool(bool1),bool(bool2))
    builder.ret(resul)
    imprimir(module,func.name,c_bool)

def ir_not(val):
    bool = ir.IntType(1)
    module = ir.Module(name="NOT_example")
    args = []
    args.append(bool)
    fnty = ir.FunctionType(bool,args)
    func = ir.Function(module,fnty,name="NOT")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    resul = builder.not_(bool(val),name=("Not"))
    builder.ret(resul)
    imprimir(module,func.name,c_bool)

def print_ir():
    #tipos
    i32 = ir.IntType(32)
    voidptr_ty = ir.IntType(8).as_pointer()
    #construccion basica    
    module = ir.Module()
    fnty = ir.FunctionType(ir.VoidType(), [])
    func = ir.Function(module, fnty, name="printer")
    
    #declarar variable
    formt = "Hola, %s! %i veces!\n\0"
    #guardar el strin como constante de IR
    c_formt = ir.Constant(ir.ArrayType(ir.IntType(8), len(formt)),
                        bytearray(formt.encode("utf8")))
    #guardar como variable global de ir
    global_formt = ir.GlobalVariable(module, c_formt.type, name="fstr")
    global_formt.linkage = 'internal'
    global_formt.global_constant = True
    global_formt.initializer = c_formt

    #argumentos
    arg = "Mundo\0"
    
    #constante con el valor del string
    c_string_val = ir.Constant(ir.ArrayType(ir.IntType(8), len(arg)),
                            bytearray(arg.encode("utf8")))

    #declarando una funcion interna printf
    printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
    printf = ir.Function(module, printf_ty, name="printf")

    #builder
    builder = ir.IRBuilder(func.append_basic_block('entry'))

    #allocar memoria y asignar la variable
    c_string = builder.alloca(c_string_val.type)
    builder.store(c_string_val, c_string)

    # asignamos un valor arbitrario al entero
    # int_val = i32(int(input("Cuantas veces? :")))
    int_val = i32(8)

    #le damos forma al argumento para el printf
    formt_arg = builder.bitcast(global_formt, voidptr_ty)
    ## llamado a la funcion printf
    builder.call(printf, [formt_arg, c_string, int_val])

    #la funcion retorna void
    builder.ret_void()

    #se imprime el modulo
    print(str(module)) 
    
    
    # este imprimir funciona mejor para este ejemplo
    llvm_module = llvm.parse_assembly(str(module))
    tm = llvm.Target.from_default_triple().create_target_machine()

    with llvm.create_mcjit_compiler(llvm_module, tm) as ee:
        ee.finalize_object()
        fptr = ee.get_function_address("printer")
        py_func = CFUNCTYPE(None)(fptr)
        py_func() 


def ir_matrix():
    # Modulo
    module = ir.Module()

    # Funcion
    function_type = ir.FunctionType(ir.VoidType(), [])
    function = ir.Function(module, function_type, name="main")
    block = function.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    # Function for printf
    printf_type = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer(), ir.DoubleType()], var_arg=True)
    printf = ir.Function(module, printf_type, name="printf")

    # Format string
    format_str = ir.GlobalVariable(module, ir.ArrayType(ir.IntType(8), len("%f %f %f\n")), name="format_str")
    format_str.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len("%f %f %f\n")), bytearray("%f %f %f\n".encode()))
    format_str.linkage = 'internal'

    # La matriz se crea como un array de 9x1 en vez de 3x3 porque asi se almacena en memoria
    matrix_values = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
    matrix_type = ir.ArrayType(ir.DoubleType(), 9)
    matrix_ptr = builder.alloca(matrix_type, name="matrix")

    # Initialize the matrix with values
    for i, value in enumerate(matrix_values):
        index = builder.gep(matrix_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
        builder.store(ir.Constant(ir.DoubleType(), value), index)

    # Print the matrix
    format_str_ptr = builder.bitcast(format_str, ir.IntType(8).as_pointer())
    for i in range(3):
        index = builder.gep(matrix_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i * 3)])
        value1 = builder.load(index)
        index = builder.gep(matrix_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i * 3 + 1)])
        value2 = builder.load(index)
        index = builder.gep(matrix_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i * 3 + 2)])
        value3 = builder.load(index)
        builder.call(printf, [format_str_ptr, value1, value2, value3])

    # Return from the function
    builder.ret_void()

    # Print the generated LLVM IR
    print(module)
    
    # este imprimir funciona mejor para este ejemplo
    llvm_module = llvm.parse_assembly(str(module))
    tm = llvm.Target.from_default_triple().create_target_machine()

    with llvm.create_mcjit_compiler(llvm_module, tm) as ee:
        ee.finalize_object()
        fptr = ee.get_function_address("main")
        py_func = CFUNCTYPE(None)(fptr)
        py_func() 


ir_matrix()