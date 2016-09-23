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

setup_files := $(venv)/.made
data_files := data/identified-people.json

#
# Targets
#

setup: $(setup_files)
data: setup $(data_files)

#
# Rules
#

#
# Data
data/identified-people.json: data/identified-people.csv
	$(python) src/cli/csv-to-json.py --input $< --output $@

#
# Setup
$(venv)/.made:
	virtualenv -q --no-site-packages -p python2.7 $(venv)
	$(pip) install pip==7.1.2 setuptools==18.2
	touch $@

$(venv)/.installed: $(venv)/.made backerequirements.txt
	$(pip) install -r requirements.txt
	touch $@
