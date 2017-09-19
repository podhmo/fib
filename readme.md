```
$ make build
mkdir -p dist
go build --buildmode=c-shared -o dist/libfib.so

$ make run
python examples/run.py
2017/09/20 07:54:46 Loaded!!
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```
