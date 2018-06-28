#!/bin/bash

rm -f report.txt
python-coverage run --branch test.py
python-coverage report -m easter.py > report.txt
python-coverage html easter.py
