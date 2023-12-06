from llvmlite import ir, binding
import llvmlite
import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int, c_float, c_bool, c_void_p, c_char_p, c_uint,cast



llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

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

#OPERACIONES BINARIAS

def add():

    # Create some useful types
    integer = ir.IntType(32)
    fnty = ir.FunctionType(integer, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="add")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    #a, b= func.args
    a = integer(3)
    b = integer (5)
    result = builder.add(a, b, name="res")
    builder.ret(result)

    # Print the module IR
    imprimir(module, "add", c_int)

def fadd():

    # Create some useful types
    float = ir.FloatType()
    fnty = ir.FunctionType(float, (float, float))

    # Create an empty module...
    module = ir.Module(name="module")
    # and declare a function named "fpadd" inside it
    func = ir.Function(module, fnty, name="fadd")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    #a, b= func.args

    a = float(3.5)
    b = float (5.3)

    result = builder.fadd(a, b, name="res")
    builder.ret(result)

    # Print the module IR
    print(module)
    imprimir(module, "fadd", c_float)

def sub():

    # Create some useful types
    integer = ir.IntType(32)
    fnty = ir.FunctionType(integer, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="sub")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(3)
    b = integer (5)
    result = builder.sub(a, b, name="res")
    builder.ret(result)

    # Print the module IR
    imprimir(module, "sub", c_int)

def fsub():

    # Create some useful types
    float = ir.FloatType()
    fnty = ir.FunctionType(float, (float, float))

    # Create an empty module...
    module = ir.Module(name="module")
    # and declare a function named "fpadd" inside it
    func = ir.Function(module, fnty, name="fsub")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = float(3.5)
    b = float (5.3)
    result = builder.fsub(a, b, name="res")
    builder.ret(result)

    # Print the module IR
    print(module)
    imprimir(module, "fsub", c_float)

def mul():

    # Create some useful types
    integer = ir.IntType(32)
    fnty = ir.FunctionType(integer, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="mul")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(3)
    b = integer (5)
    result = builder.mul(a, b, name="res")
    builder.ret(result)

    # Print the module IR
    imprimir(module, "mul", c_int)

def fmul():

    # Create some useful types
    float = ir.FloatType()
    fnty = ir.FunctionType(float, (float, float))

    # Create an empty module...
    module = ir.Module(name="module")
    # and declare a function named "fpadd" inside it
    func = ir.Function(module, fnty, name="fmul")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = float(3.5)
    b = float (5.3)
    result = builder.fmul(a, b, name="res")
    builder.ret(result)

    # Print the module IR
    print(module)
    imprimir(module, "fmul", c_float)

def div():

    # Create some useful types
    integer = ir.IntType(32)
    fnty = ir.FunctionType(integer, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="div")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(15)
    b = integer (5)
    result = builder.sdiv(a, b, name="res")
    builder.ret(result)


    # Print the module IR
    imprimir(module, "div", c_int)

def fdiv():

    # Create some useful types
    float = ir.FloatType()
    fnty = ir.FunctionType(float, (float, float))

    # Create an empty module...
    module = ir.Module(name="module")
    # and declare a function named "fpadd" inside it
    func = ir.Function(module, fnty, name="fdiv")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = float(3.5)
    b = float (5.3)
    result = builder.fdiv(a, b, name="res")
    builder.ret(result)

    # Print the module IR
    print(module)
    imprimir(module, "fdiv", c_float)

def operacionesBinarias():
    add()
    fadd()
    sub()
    fsub()
    mul()
    fmul()
    div()
    fdiv()

#COMPARACIONES

def biggerThan():

    # Create some useful types
    integer = ir.IntType(32)
    bool = ir.IntType(1)
    fnty = ir.FunctionType(bool, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="biggerThan")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(5)
    b = integer (15)
    result = builder.icmp_signed('>', a, b)
    builder.ret(result)


    # Print the module IR
    imprimir(module, func.name, c_bool)

def biggerThanOrEqual():

    # Create some useful types
    integer = ir.IntType(32)
    bool = ir.IntType(1)
    fnty = ir.FunctionType(bool, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="biggerThanOrEqual")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(5)
    b = integer (5)
    result = builder.icmp_signed('>=', a, b)
    builder.ret(result)


    # Print the module IR
    imprimir(module, func.name, c_bool)

def lessThan():

    # Create some useful types
    integer = ir.IntType(32)
    bool = ir.IntType(1)
    fnty = ir.FunctionType(bool, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="lessThan")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(5)
    b = integer (15)
    result = builder.icmp_signed('<', a, b)
    builder.ret(result)


    # Print the module IR
    imprimir(module, func.name, c_bool)

def lessThanOrEqual():

    # Create some useful types
    integer = ir.IntType(32)
    bool = ir.IntType(1)
    fnty = ir.FunctionType(bool, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="lessThanOrEqual")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(5)
    b = integer (5)
    result = builder.icmp_signed('<=', a, b)
    builder.ret(result)


    # Print the module IR
    imprimir(module, func.name, c_bool)

def equal():

    # Create some useful types
    integer = ir.IntType(32)
    bool = ir.IntType(1)
    fnty = ir.FunctionType(bool, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="equal")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(5)
    b = integer (5)
    result = builder.icmp_signed('==', a, b)
    builder.ret(result)


    # Print the module IR
    imprimir(module, func.name, c_bool)

def different():

    # Create some useful types
    integer = ir.IntType(32)
    bool = ir.IntType(1)
    fnty = ir.FunctionType(bool, (integer, integer))

    # Create an empty module...
    module = ir.Module(name="module")
    func = ir.Function(module, fnty, name="different")

    # Now implement the function
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    a = integer(5)
    b = integer (4)
    result = builder.icmp_signed('!=', a, b)
    builder.ret(result)


    # Print the module IR
    imprimir(module, func.name, c_bool)

def comparaciones():
    biggerThan()
    biggerThanOrEqual()
    lessThan()
    lessThanOrEqual()
    equal()
    different()
#CONDICIONALES


def ifStmt():
    i32 = ir.IntType(32)
    func_name = "ifStmt"
    mod = ir.Module()
    i32 = ir.IntType(32)

    fn = ir.Function(mod, ir.FunctionType(i32, [i32, i32]), func_name)

    builder = ir.IRBuilder(fn.append_basic_block())
    [x, y] = fn.args
    x.name = 'x'
    y.name = 'y'
    x_lt_y = builder.icmp_signed('<', x, y)
    with builder.if_else(x_lt_y) as (then, orelse):
        with then:
            bb_then = builder.basic_block
            out_then = builder.sub(y, x, name='out_then')
        with orelse:
            bb_orelse = builder.basic_block
            out_orelse = builder.sub(x, y, name='out_orelse')

    out_phi = builder.phi(i32)
    out_phi.add_incoming(out_then, bb_then)
    out_phi.add_incoming(out_orelse, bb_orelse)

    builder.ret(out_phi)
    
    print(out_orelse)
    print(out_then)
    #imprimir(mod,func_name, c_void_p)

def condicionales():
    ifStmt()

#CICLOS

def whileStmt():

    i32 = ir.IntType(32) #integer with 32 bits

    #make a module
    module = ir.Module(name = "module")

    # define function parameters for function "main"
    return_type = i32 #return int
    argument_types = list() #can add ir.IntType(#), ir.FloatType() for arguments
    func_name = "whileStmt"

    #make a function
    fnty = ir.FunctionType(return_type, argument_types)
    while_func = ir.Function(module, fnty, name=func_name)

    # append basic block named 'entry', and make builder
    # blocks generally have 1 entry and exit point, with no branches within the block
    block = while_func.append_basic_block('entry')
    builder = ir.IRBuilder(block)


    ########################################
    # symbol table generation, key = variable name, value = pointer

    x_value = ir.Constant(i32, 3) #create the values
    i_value = ir.Constant(i32, 1)
    x_pointer = builder.alloca(i32) #create the addresses
    i_pointer = builder.alloca(i32)
    builder.store(x_value, x_pointer) #store those values at those addresses
    builder.store(i_value, i_pointer)

    symbol_table ={"x":x_pointer, "i":i_pointer}

    ##########################################
    # while loop.

    w_body_block = builder.append_basic_block("w_body")
    w_after_block = builder.append_basic_block("w_after")

    # head
    # initial checking of while (i < 5)
    constant_5 = ir.Constant(i32, 5)
    current_i_value = builder.load(symbol_table["i"]) #loads the value of i_pointer
    cond_head = builder.icmp_signed('<', current_i_value, constant_5, name="lt") #returns boolean, which is ir.IntType(1)

    #for the first checking of (i<5), it could go straight from the the head to w_after_block
    # if i is already greater than 5. It needs to check whether to start the loop at all.
    builder.cbranch(cond_head, w_body_block, w_after_block)

    # body
    builder.position_at_start(w_body_block)
    current_x_value = builder.load(symbol_table["x"])
    current_i_value = builder.load(symbol_table["i"])

    # x = x * 2
    # i = i + 1
    new_x_value = builder.mul(current_x_value, ir.Constant(i32, 2), name='mul')
    new_i_value = builder.add(current_i_value, ir.Constant(i32,1), name="add")
    builder.store(new_x_value, symbol_table["x"]) #store the new x value at the x pointer
    builder.store(new_i_value, symbol_table["i"])

    #at the end of the w_body_block, you need to check i < 5 again, because there's a branch possibility
    # if true, it returns to the top of the w_body_block. If false, it exits the loop
    cond_body = builder.icmp_signed('<', new_i_value, constant_5, name="lt")
    builder.cbranch(cond_body, w_body_block, w_after_block)
    # after
    builder.position_at_start(w_after_block)

    ##############################
    # return x
    x_address = symbol_table["x"]
    x_value = builder.load(x_address)
    # we return this value

    builder.ret(x_value)
    #print(module)
    imprimir(module,func_name, c_int)

def for_code_ir():
        binding.initialize()
        binding.initialize_native_target()
        binding.initialize_native_asmprinter()

      #Create an LLVM module
        miModulo = ir.Module()

        # Create a function  "simple_loop"
        bucleSimpleFunction = ir.Function(miModulo, ir.FunctionType(ir.IntType(32), []), name="ForCodeIR")

        # Create basic blocks
        entryBlock = bucleSimpleFunction.append_basic_block(name="entry")
        bodyBlock = bucleSimpleFunction.append_basic_block(name="body")
        afterBlock = bucleSimpleFunction.append_basic_block(name="after")

         # Start construction of IR
        builder = ir.IRBuilder(entryBlock)

        # calculate return value
        result = builder.alloca(ir.IntType(32), name="result")
        builder.store(ir.Constant(ir.IntType(32), 0), result)

        # Start for
        builder.branch(bodyBlock)

        # Build the loop bodyBuild the loop body
        builder.position_at_end(bodyBlock)
        index = builder.load(result)
        newValue = builder.add(index, ir.Constant(ir.IntType(32), 1))
        builder.store(newValue, result)
        condition = builder.icmp_unsigned('==', newValue, ir.Constant(ir.IntType(32), 10))
        builder.cbranch(condition, afterBlock, bodyBlock)

        # build block after loop
        builder.position_at_end(afterBlock)

        # Return result
        finalResult = builder.load(result)
        builder.ret(finalResult)

        print(str(miModulo))

# Llamar al método for
def ciclos():
    whileStmt()
    for_code_ir()

#DECLARACIONES#

#enteros de 32 bits
def int_decl():
    i32 = ir.IntType(32)
    module = ir.Module(name="module")
    fnty = ir.FunctionType(i32,[])
    func = ir.Function(module,fnty,name= "int_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = i32
    builder.alloca(var_type, name="intVar")
    print(module)

#Punto flotante de precision simple
def float_decl():
    f32 = ir.FloatType()
    module = ir.Module(name="module")
    fnty = ir.FunctionType(f32,[])
    func = ir.Function(module,fnty,name= "float_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = f32
    builder.alloca(var_type, name="floatVar")
    print(module)

#Que es un string, mas que un arreglo de chars
#Que es un char mas que un entero de 8 bits traducido
def string_decl():
    char = ir.IntType(8)
    string = ir.ArrayType(char,0)
    module = ir.Module(name="module")
    fnty = ir.FunctionType(string,[])
    func = ir.Function(module,fnty,name= "string_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = string
    builder.alloca(var_type, name="stringVar")
    print(module)

#Entero de 1 bit, 0 = false, 1 = true
def bool_decl():
    bool = ir.IntType(1)
    module = ir.Module(name="module")
    fnty = ir.FunctionType(bool,[])
    func = ir.Function(module,fnty,name= "bool_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = bool
    builder.alloca(var_type, name="boolVar")
    print(module)

def declaraciones():
    int_decl()
    float_decl()
    string_decl()
    bool_decl()


#ASIGNACIONES#

def int_asign(val):
    i32 = ir.IntType(32)
    module = ir.Module(name="module")
    fnty = ir.FunctionType(i32,[])
    func = ir.Function(module,fnty,name= "int_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = i32
    int_var = builder.alloca(var_type, name="intVar")
    int_val = i32(val)
    builder.store(int_val,int_var)
    builder.ret(int_val)
    imprimir(module,func.name,c_int)

def float_asign(val):
    f32 = ir.FloatType()
    module = ir.Module(name="module")
    fnty = ir.FunctionType(f32,[])
    func = ir.Function(module,fnty,name= "float_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = f32
    float_var = builder.alloca(var_type, name="floatVar")
    float_val = f32(val)
    builder.store(float_val,float_var)
    builder.ret(float_val)
    imprimir(module,func.name,c_float)

def string_asign(val):
    char = ir.IntType(8)
    string = ir.ArrayType(char,len(val))
    string_arg = []
    for value in val:
        string_arg.append(ord(value))
    module = ir.Module(name="module")
    fnty = ir.FunctionType(string,[])
    func = ir.Function(module,fnty,name= "string_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = string
    string_var = builder.alloca(var_type, name="stringVar")
    string_val = string(string_arg)
    builder.store(string_val,string_var)
    builder.ret(string_val)
    print(module)

def bool_asign(val):
    bool = ir.IntType(1)
    module = ir.Module(name="module")
    fnty = ir.FunctionType(bool,[])
    func = ir.Function(module,fnty,name= "bool_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = bool
    bool_var = builder.alloca(var_type, name="boolVa-r")
    bool_val = bool(val)
    builder.store(bool_val,bool_var)
    builder.ret(bool_val)
    imprimir(module,func.name,c_bool)

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

def asignaciones():
    int_asign(1337)
    float_asign(42.1337)
    string_asign("Hola Mundo")
    bool_asign(True)
    array(23,32,33,1)
    ir_matrix()

#OPERADORES LOGICOS

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

def operadoresLogicos():
    ir_and(True,True)
    ir_or(False,False)
    ir_not(True)
#ENTRADA/SALIDA

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

    #declarando funcion interna printf
    printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
    printf = ir.Function(module, printf_ty, name="printf")

    #builder
    builder = ir.IRBuilder(func.append_basic_block('entry'))

    #allocar memoria y asignar la variable
    c_string = builder.alloca(c_string_val.type)
    builder.store(c_string_val, c_string)

    # asignamos un valor arbitrario al entero
    int_val = i32(8)
    
    #le damos forma al argumento para el printf
    formt_arg_printf = builder.bitcast(global_formt, voidptr_ty)
    
    ## llamado a la funcion printf
    builder.call(printf, [formt_arg_printf, c_string, int_val])

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

def scan_ir():
    i32 = ir.IntType(32)
    char = ir.IntType(8)
    voidptr_ty = ir.IntType(8).as_pointer()
    module = ir.Module()
    fnty = ir.FunctionType(ir.VoidType(), [])
    func = ir.Function(module, fnty, name="scanner")
    builder = ir.IRBuilder(func.append_basic_block('entry'))
    
    #declarando funcion interna printf
    printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
    printf = ir.Function(module, printf_ty, name="printf")
    
    #declarando funcion interna scanf
    scanf_ty = ir.FunctionType(i32,[voidptr_ty],var_arg=True)
    scanf = ir.Function(module,scanf_ty,name= "scanf")
    
    formt = "Value is: %d\0"
    
    formt_str = ir.Constant(ir.ArrayType(char, len(formt)),
                        bytearray(formt.encode("utf8")))
    
    #guardar como variable global de ir
    global_formt = ir.GlobalVariable(module, formt_str.type, name="input_int")
    global_formt.linkage = 'internal'
    global_formt.global_constant = True
    global_formt.initializer = formt_str
    
    formt_str_ptr = builder.bitcast(global_formt, voidptr_ty)
    
    val = builder.alloca(char,name= 'Valor')
    
    builder.call(scanf,[formt_str_ptr,val])
    
    loaded_val = builder.load(val, name='Valor')
    
    builder.call(printf,[formt_str_ptr,loaded_val])
    #la funcion retorna void
    builder.ret_void()

    #se imprime el modulo
    print(str(module)) 
    
    # este imprimir funciona mejor para este ejemplo
    llvm_module = llvm.parse_assembly(str(module))
    tm = llvm.Target.from_default_triple().create_target_machine()

    with llvm.create_mcjit_compiler(llvm_module, tm) as ee:
        ee.finalize_object()
        fptr = ee.get_function_address("scanner")
        py_func = CFUNCTYPE(None)(fptr)
        py_func() 

def entradaSalida():
    print_ir()
    scan_ir()

#operacionesBinarias()
#comparaciones()
#condicionales()
ciclos()
#declaraciones()
#asignaciones()
#operadoresLogicos()
#entradaSalida()