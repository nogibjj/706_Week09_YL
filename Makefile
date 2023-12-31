install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py

test:
	python -m pytest -vv --cov=main test_*.py
	py.test --nbval-lax *.ipynb