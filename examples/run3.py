import ctypes
import ctypes.util as u
fib = ctypes.CDLL(u.find_library('fib'))
fib.fib.argtypes = [ctypes.c_int]
fib.fib.restype = ctypes.c_int
L = range(11)
print([fib.fib(x) for x in L])
