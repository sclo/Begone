.PHONY: build

build:
	python -m begone_convert.convert data/numbers.yaml dist/fr-all.xml
