```
$ make build
mkdir -p dist
go build -buildmode=c-shared -ldflags="-extldflags -Wl,-soname,libfib.so" -o dist/libfib.so

$ make run
python examples/run.py
2017/09/20 07:54:46 Loaded!!
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

only mac version

```
$ DYLD_FALLBACK_LIBRARY_PATH=dist python -c "import ctypes.macholib.dyld as d; print(d.dyld_fallback_library_path())"
dist
$ DYLD_FALLBACK_LIBRARY_PATH=dist python -c "import ctypes.macholib.dyld as d; print(d.dyld_find('libfib.dylib'))"
dist/libfib.dylib
$ DYLD_FALLBACK_LIBRARY_PATH=dist python -c "import ctypes.util as u; print(u.find_library('libfib'))"
dist/libfib.dylib
$ DYLD_FALLBACK_LIBRARY_PATH=dist python -c "import ctypes.util as u; print(u.find_library('fib'))"
```

linux

```
$ LD_LIBRARY_PATH=dist python -c 'import ctypes.util as u; print(u._findLib_ld("fib"))'
dist/libfib.so
$ LD_LIBRARY_PATH=dist python -c 'import ctypes.util as u; print(u.find_library("fib"))'
$ objdump -p -j .dynamic dist/libfib.so | grep -i soname
  SONAME               libfib.so
```
