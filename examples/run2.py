import ctypes
import os.path

fib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "../dist/libfib.so"))
# stack overflow
fib.fib("foo")
