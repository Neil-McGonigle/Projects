
class Person:	
	def __init__(self, obj):
		self.personid = obj['person_id']
 		self.title = obj['title']
 		self.surname = obj['surname']
 		self.forename = obj['forename']

 	def __repr__(self):
 		return '<Person %r>' % (self.personid) % (self.title) % (self.surname)





