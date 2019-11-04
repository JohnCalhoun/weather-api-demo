init:
	pip3 install -r requirements.txt

test:
	python3 -m unittest discover tests -v

docs: 
	cd docs; pydocmd build

.PHONY: init test docs
