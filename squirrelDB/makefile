SHELL := /bin/bash

install:
	pip3 install --upgrade virtualenv  
activate:
	source venv/bin/activate  
dependencies:
	pip3 install -r requirements.txt 
migration:
	python3 manage.py makemigrations
migrate:
	python3 manage.py migrate
run:
	python3 manage.py runserver