### Required setup
import ctypes 
my_lib = ctypes.CDLL("./my_test.so")
 
### Test 1
print "Test 1: Send/Return string to/from C program"
# restype is must, or python will print integer instead of string
my_lib.hello.restype = ctypes.c_char_p
w = "John"
txt = my_lib.hello(w)
print(txt)
print '------------------------------'
 
### Test 2
print "Test 2: Send/Return integer to/from C program"
a = 5
b = 10
result = my_lib.addNum(a,b)
print a,"+",b,"=",result
print '------------------------------'

### Test 3
print "Test 3: Return float from C program"
my_lib.add_float.restype = ctypes.c_float
my_lib.add_float.argtypes = [ctypes.c_float, ctypes.c_float]
result = my_lib.add_float(6.5, 7.9)
print('%.2f'%result) 
print '------------------------------'

### Test 4.1
print "Test 4.1: Array operations"
a = (ctypes.c_int * 3) (-1, 2, 5)
b = (ctypes.c_int * 3) (-2, 3, 4)
res = (ctypes.c_int * 3) (0, 0, 0)
n = ctypes.c_int(3) 
my_lib.add_int_array(a,b,res,n)
print " A :",a[0],":",a[1],":",a[2]
print " B :",b[0],":",b[1],":",b[2]
print "A+B:",res[0],":",res[1],":",res[2]
print '------------------------------'

### Test 4.2
print "Test 4.2: Array operations : Using numpy"
import numpy as np
a = np.array([-1, 2, 5], dtype=ctypes.c_int)
b = np.array([-2, 3, 4], dtype=ctypes.c_int)
res = np.zeros(3, dtype=ctypes.c_int)
n = ctypes.c_int(3)
intp = ctypes.POINTER(ctypes.c_int)

i = a.ctypes.data_as(intp)
j = b.ctypes.data_as(intp)
k = res.ctypes.data_as(intp)
my_lib.add_int_array(i,j,k,n)
print " A :",a
print " B :",b
print "A+B:",res

### Test 5
print "Test 5: Array operations : Using numpy"
a = np.array([-2.22, 4.44, 8.88], dtype=ctypes.c_float)
b = np.zeros(3, dtype=ctypes.c_float)
n = ctypes.c_int(3)
intp = ctypes.POINTER(ctypes.c_float)

i = a.ctypes.data_as(intp)
j = b.ctypes.data_as(intp)
my_lib.array_div(i,j,n)
print " A :",a
print " B :",b
