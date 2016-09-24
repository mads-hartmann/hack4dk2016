ifeq ($(shell which python),)
$(error You need python, brew install python)
endif

ifeq ($(shell which virtualenv),)
$(error You need virtualenv, run pip install virtualenv)
endif

#
# Variables
#

venv := _venv
pip := $(venv)/bin/pip
python := $(venv)/bin/python
ipython := $(venv)/bin/ipython2
jupyter-notebook := $(venv)/bin/jupyter-notebook

setup_files := $(venv)/.installed
data_files := data/identified-people.json

#
# Targets
#

setup: $(setup_files)
data: setup $(data_files)
run: data; PYTHONPATH=src $(python) src/web/main.py
console: data; PYTHONPATH=src $(ipython)
notebook: data; PYTHONPATH=$(PWD)/src $(jupyter-notebook) notebook/data.ipynb
db_import: ; PYTHONPATH=$(PWD)/src $(python) src/cli/csv_to_db.py --input data/identified-people.csv

#
# Rules
#

#
# Data
data/identified-people.json: data/identified-people.csv
	$(python) src/cli/csv_to_json.py --input $< --output $@

#
# Setup
$(venv)/.made:
	virtualenv -q --no-site-packages -p python2.7 $(venv)
	$(pip) install pip==8.1.2 setuptools==18.2
	touch $@

$(venv)/.installed: $(venv)/.made requirements.txt
	$(pip) install -r requirements.txt
	touch $@
