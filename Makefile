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
	python setup.py sdist
	ls -l dist

