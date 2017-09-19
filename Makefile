build:
	mkdir -p dist
	go build --buildmode=c-shared -o dist/libfib.so

clean:
	rm -rf dist

run:
	python examples/run.py
