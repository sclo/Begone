.PHONY: build init

build:
	begone-convert data/numbers.yaml dist/begone-fr-tout.xml all
	begone-convert data/numbers.yaml dist/begone-fr-demarchage.xml spam
	begone-convert data/numbers.yaml dist/begone-fr-voip.xml voip
	begone-convert data/numbers.yaml dist/begone-fr-onoff.xml onoff
	begone-convert data/numbers.yaml dist/begone-fr-ubicentrex.xml ubicentrex

init:
	uv venv
	uv sync
