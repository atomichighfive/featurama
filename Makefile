all	:
	python3 setup.py sdist bdist_wheel

clean	:
	rm -rf ./dist/
	rm -rf featurama_atomichighfive.egg-info/
	rm -rf build/
