PORT:=8080
PYTHON:=python
HOST:=0.0.0.0

run:
	${PYTHON} src/main.py --port ${PORT} --host ${HOST}