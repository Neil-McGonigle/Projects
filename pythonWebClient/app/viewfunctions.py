import requests
import json
from flask import render_template, flash, redirect, request
from app import app
from forms import LoginForm, PeopleUnionForm
from models import Person


def getPerson(form):
	#put this in a global configuration file
	url = 'http://user:user@95.138.170.205:8080/odata/EmployeePeopleVDB2/People_union'
 	url = url + '(' + form.personid.data + ')'
 	url = url + '?$format=json'
 	r = requests.get(url)
 	data = r.json()
 	obj = data['d']
 	flash('Attempt to get the person via an oData request and display:' + form.personid.data)
	person = Person(obj) 	
	flash('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	flash(str(person.personid) +  ' ' + person.title + ' ' + person.forename +  ' ' + person.surname)

