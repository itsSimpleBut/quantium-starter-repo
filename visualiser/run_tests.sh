#!/bin/bash
source ../venv/Scripts/activate
pytest test_app_components.py -v
exit $?

