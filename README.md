# LSH
Python implementation of nearest-neighbour search using locality-sensitive hashing (LSH)

## Installation
In order to run the program, Python >= 3.9 is required together with the dependencies specified in the `requirements.txt`. You can install them using `pip install -r requirements.txt`

To test different aspects of the program, use
```bash
python -m unittest tests.test_shingling
python -m unittest tests.test_minhash
python -m unittest tests.test_LSH
```

## Generate your own requirements file
The projects uses [pip-tools] to generate a requirements file based on the dependencies specified in `pyproject.toml`. To generate your own requirements file (e.g. for a different version of Python) install pip-tools and run
```bash
pip-compile -o requirements.txt pyproject.toml
``` 
