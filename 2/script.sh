#!/bin/bash
rm -f htmlcov/
rm -f report.txt
python-coverage run --branch test.py
python-coverage report -m irpef.py > report.txt
python-coverage html irpef.py
