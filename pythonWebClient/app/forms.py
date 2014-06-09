from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class LoginForm(Form):
	openid = TextField('openid', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)

class PeopleUnionForm(Form):
	personid = TextField('personid', validators = [Required()])
	#title = TextField('title', validators = [Required()])
	#forename = TextField('forename', validators = [Required])
	#suranme = TextField('surname', validators = [Required])

