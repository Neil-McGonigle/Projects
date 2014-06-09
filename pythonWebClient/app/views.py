import requests
import json
import viewfunctions
from flask import render_template, flash, redirect, request
from app import app
from forms import LoginForm, PeopleUnionForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Miguel'} #fake user
	posts = [ # fake array for demo
		{
			'author': { 'nickname': 'John' },
			'body': 'Beautiful day in Glasghow!'
		},
		{
			'author': {'nickname': 'Susan' },
			'body': 'Dont diss the Dostoyevski!'
		}
	]

	return render_template("index.html",
		title = 'CPP Demo',
		user = user,
		posts = posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Sign In',
        form = form)


@app.route('/people', methods = ['GET', 'POST'])
def people():
 	form = PeopleUnionForm()
 	if form.validate_on_submit(): 		
 		viewfunctions.getPerson(form)
 		return redirect('/people')
 	return render_template('peopleUnion.html',
 		title = 'People',
 		form = form)

