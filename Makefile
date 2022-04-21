PORT:=8080
_PYTHONPATH:=PYTHONPATH=./src
PYTHON:=${_PYTHONPATH} python
HOST:=0.0.0.0

install:
	pip install -r requirements.txt

run:
	${PYTHON} src/main.py --port ${PORT} --host ${HOST}

init-db:
	${PYTHON} src/database/connection.py