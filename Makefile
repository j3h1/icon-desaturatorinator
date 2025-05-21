run: .vpython/ main.py 
	.vpython/bin/python main.py	/usr/share/icons/

venv: /usr/bin/python
	python -m venv .vpython

clean:
	rm -rf .vpython/
