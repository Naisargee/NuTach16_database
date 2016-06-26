import cgi
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class NewEntry(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('main.html')
        self.response.write(template)

class Conformation(webapp2.RequestHandler):
	def get(self):
		self.response.write("hello")

    def post(self):
        email = self.request.get('email')
        password = self.request.get('password')

        query_params = {'guestbook_name': guestbook_name}
        self.redirect('/?' + urllib.urlencode(query_params))

        template_values={
            'email' : email
            'passwor'd : password
        }

        template = JINJA_ENVIRONMENT.get_template('conformation.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/NewEntry', NewEntry),
    ('/Conformation', Conformation),
], debug=True)
