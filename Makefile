init:
	pip3 install -r requirements.txt

test:
	python3 -m unittest discover tests

.PHONY: init test
