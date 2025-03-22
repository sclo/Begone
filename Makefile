.PHONY: build init

build:
	begone-convert data/numbers.yaml dist/begone-fr-full.xml all
	begone-convert data/numbers.yaml dist/begone-fr-demarchage.xml spam
	begone-convert data/numbers.yaml dist/begone-fr-voip.xml voip
	begone-convert data/numbers.yaml dist/begone-fr-prepaid.xml prepaid
	begone-convert data/numbers.yaml dist/begone-fr-onoff.xml onoff
	begone-convert data/numbers.yaml dist/begone-fr-ubicentrex.xml ubicentrex
	begone-convert data/numbers.yaml dist/begone-fr-lyca.xml lyca
	begone-convert data/numbers.yaml dist/begone-fr-aircall.xml aircall
	begone-convert data/numbers.yaml dist/begone-fr-bjt.xml bjt
	begone-convert data/numbers.yaml dist/begone-fr-kavcom.xml kavcom

init:
	uv venv
	uv sync
