.PHONY: build

build:
	python -m begone_convert.convert data/numbers.yaml dist/begone-fr-tout.xml       all
	python -m begone_convert.convert data/numbers.yaml dist/begone-fr-demarchage.xml spam
	python -m begone_convert.convert data/numbers.yaml dist/begone-fr-voip.xml       voip
	python -m begone_convert.convert data/numbers.yaml dist/begone-fr-onoff.xml      onoff
	python -m begone_convert.convert data/numbers.yaml dist/begone-fr-ubicentrex.xml ubicentrex
