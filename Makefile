init:
	pip3 install -r requirements.txt

test:
	python3 -m unittest discover tests -v

docs: 
	cd docs; pydocmd build

upload:
	aws s3 sync docs/html s3://weather-api-demo

.PHONY: init test docs upload
