#!/bin/bash

python-coverage run --branch test.py

python-coverage report -m codiceFiscale.py > report.txt

python-coverage html codiceFiscale.py
