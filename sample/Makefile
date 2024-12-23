
# define the name of the virtual environment directory
VENV := .venv
TEST=
PARAMETERS=

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate:

# venv is a shortcut target
venv: $(VENV)/bin/activate
	python3 -m virtualenv $(VENV)
	python3 -m pipenv shell

install:
	pipenv install

run:
	pipenv run python -m thalia ${PARAMETERS}

build:
	pipenv run python build ${PARAMETERS}

test: build
	pipenv run python -m pytest ${TEST}

clean:
	pipenv --rm
	rm -rf {$(VENV),build,dist,logs/*};rm -rf .pytest_cache;find . -type f -name '*.pyc' -delete

lint:
	 pipenv run python -m black --target-version=py35 thalia setup.py
	 pipenv run python -m flake8 thalia setup.py

d-build:
	docker-compose build

d-up:
	docker-compose up -d --build

d-ls:
	docker-compose ps

d-logs:
	docker-compose logs -f --tail 15

d-clean:
	docker-compose down && docker-compose rm

d-down:
	docker-compose down

