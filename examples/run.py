import ctypes
import os.path

fib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../dist/libfib.so"))

L = range(11)
print([fib.fib(x) for x in L])
