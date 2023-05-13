# advanced-testing-techniques

tthis is repo for doing advances testing

##Setup Project


1. Create and source virtual envireonment

```bash
virtualenv ~/.advanced-testing
source ~/.advanced-testint/bin/activate
```

2. create scaffold

``bash
touch Makefile && touch test_hello.py && touch hello.py  && requirements.txt
```

3. Populate `Makefile`

```bash
install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv -vvcov=hello --cov=hellocli test_hello.py

lint:
	pylint --disable=R,C hello.py hellocli.py

all: install lint test
```

### How to debug
* Print
* pdb
* testing
