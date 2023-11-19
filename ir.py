from llvmlite import ir
import llvmlite
import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int, c_float


llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()


#DECLARACIONES#

#enteros de 32 bits
def int_decl():
    i32 = ir.IntType(32)
    module = ir.Module(name="INT_Declaration")
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
    module = ir.Module(name="Float_Declaration")
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
    module = ir.Module(name="String_Declaration")
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
    module = ir.Module(name="Bool_Declaration")
    fnty = ir.FunctionType(bool,[])
    func = ir.Function(module,fnty,name= "bool_decl")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = bool
    builder.alloca(var_type, name="boolVar")
    print(module)

def array_decl(type):
    if(type == "int"): 
        arr_type = ir.IntType(32)
    elif(type == "float"): 
        arr_type = ir.FloatType()
    elif(type == "bool"): 
        arr_type = ir.IntType(1)
        
    

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
    var_type = i32
    int_var = builder.alloca(var_type, name="intVar")
    int_val = i32(val)
    builder.store(int_val,int_var)
    print(module)

#asignar valor a flotante
def float_asign(val):
    f32 = ir.FloatType()
    module = ir.Module(name="Float_Asign")
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
    module = ir.Module(name="String_Asign")
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
    module = ir.Module(name="Bool_Asign")
    fnty = ir.FunctionType(bool,[])
    func = ir.Function(module,fnty,name= "int_asign")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    var_type = bool
    bool_var = builder.alloca(var_type, name="boolVar")
    bool_val = bool(val)
    builder.store(bool_val,bool_var)
    print(module)

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
    print(module)
    
def ir_or(bool1,bool2):
    bool = ir.IntType(1)
    module = ir.Module(name="OR_example")
    fnty = ir.FunctionType(bool,(bool,bool))
    func = ir.Function(module,fnty,name="OR")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    resul = builder.or_(bool(bool1),bool(bool2))
    builder.ret(resul)
    print(module)

def ir_not(val):
    bool = ir.IntType(1)
    module = ir.Module(name="NOT_example")
    args = []
    args.append(bool)
    fnty = ir.FunctionType(bool,args)
    func = ir.Function(module,fnty,name="NOT")
    block = func.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)
    resul = builder.not_(bool(val))
    builder.ret(resul)
    print(resul)
    print(module)
    

ir_not(True)

