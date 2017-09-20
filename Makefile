build:
	mkdir -p dist
	go build -buildmode=c-shared -ldflags="-extldflags -Wl,-soname,libfib.so" -o dist/libfib.so

clean:
	rm -rf dist

run:
	LD_LIBRARY_PATH=dist DYLD_FALLBACK_LIBRARY_PATH=dist python examples/run3.py
