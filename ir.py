from llvmlite import ir
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

def whileStmt():
    i32 = ir.IntType(32) #integer with 32 bits

    #make a module
    module = ir.Module(name = "module")

    # define function parameters for function "main"
    return_type = i32 #return int
    argument_types = list() #can add ir.IntType(#), ir.FloatType() for arguments
    func_name = "main"

    #make a function
    fnty = ir.FunctionType(return_type, argument_types)
    main_func = ir.Function(module, fnty, name=func_name)

    # append basic block named 'entry', and make builder
    # blocks generally have 1 entry and exit point, with no branches within the block
    block = main_func.append_basic_block('entry')
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

def decl():
    int_decl()
    float_decl()
    string_decl()
    bool_decl()

#ASIGNACIONES#

#Asignar valor a entero de 32 bits 
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
    print(module)

#asignar valor a flotante
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
    print(module)    

#asignar valor a string
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
    print(module)

#asignar valor a bool
def bool_asign(val):
    bool = ir.IntType(1)
    module = ir.Module(name="module")
    fnty = ir.FunctionType(bool,[])
    func = ir.Function(module,fnty,name= "int_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = bool
    bool_var = builder.alloca(var_type, name="boolVa-r")
    if(val == True):
        bool_val = bool(1) #True = 1
    elif(val == False):
        bool_val = bool(0) #False = 0
    builder.store(bool_val,bool_var)
    print(module)

def asign():
    int_asign(1337)
    float_asign(42.1337)
    string_asign("Hola Mundo")
    bool_asign(True)


#decl()    
#asign()
#ifStmt()
#whileStmt()
#add()
#fadd()
#sub()
#fsub()
#mul()
#fmul()
#div()
#fdiv()
equal()
different()