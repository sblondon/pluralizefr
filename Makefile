help:
	@echo "Available targets:"
	@echo "check - run tests"
	@echo "clean - remove generated files"

check:
	python setup.py test

clean:
	find . -name '*.pyc' -delete 
	rm -rf *.egg-info

