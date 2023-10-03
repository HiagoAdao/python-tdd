clean:
	-rm -rf ./__pycache__
	-rm -rf ./**/__pycache__
	-rm -rf ./**/**/__pycache__

test:
	-pytest tests -v

