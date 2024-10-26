help:
	@echo "Available targets:"
	@echo "check - run tests"
	@echo "clean - remove generated files"
	@echo "dist - create library archive"

check:
	python setup.py test

clean:
	find . -name '*.pyc' -delete 
	rm -rf *.egg-info
	rm -rf dist

dist: clean
	python3 -m venv venv
	. ./venv/bin/activate
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade build
	python3 -m build
	ls -l dist

publish:
	. ./venv/bin/activate
	python3 -m pip install --upgrade twine