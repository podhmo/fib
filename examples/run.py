import ctypes
import os.path

fib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../dist/libfib.so"))
fib.fib.argtypes = [ctypes.c_int]
fib.fib.restype = ctypes.c_int
L = range(11)
print([fib.fib(x) for x in L])
