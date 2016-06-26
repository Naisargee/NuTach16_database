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

allowed_users=["13bce130@nirmauni.ac.in"]
showAll_users=["13bce130@nirmauni.ac.in"]

#allowed_users=#["13bce074@nirmauni.ac.in","14bce043@nirmauni.ac.in","14bce030@nirmauni.ac.in","14bce046@nirmauni.ac.in","14bce071@nirmauni.ac.in","14bce119@nirmauni.ac.in","14bce036@nirmauni.ac.in","14bce024@nirmauni.ac.in","14bce029@nirmauni.ac.in","13bce081@nirmauni.ac.in","13bce066@nirmauni.ac.in","13bce109@nirmauni.ac.in","13bce130@nirmauni.ac.in","13bce035@nirmauni.ac.in","14bce127@nirmauni.ac.in","14bce009@nirmauni.ac.in","13bce007@nirmauni.ac.in","13bce063@nirmauni.ac.in","13bit032@nirmauni.ac.in","13bit033@nirmauni.ac.in","13bit053@nirmauni.ac.in","13bit55nirmauni.ac.in","14mca59@nirmauni.ac.in","14mca42@nirmauni.ac.in","14mca01@nirmauni.ac.in","14mca21@nirmauni.ac.in","14mca07@nirmauni.ac.in","14mca19@nirmauni.ac.in"]
#showAll_users=["13bce081@nirmauni.ac.in","13bce007@nirmauni.ac.in","13bce130@nirmauni.ac.in"]

##################################################### Tutorial Example ################################################################

#class MainPage(webapp2.RequestHandler):
#
#    def get(self):
#        guestbook_name = self.request.get('guestbook_name',
#                                          DEFAULT_GUESTBOOK_NAME)
#        greetings_query = Greeting.query(
#            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
#        greetings = greetings_query.fetch(10)
#
#        user = users.get_current_user()
#        if user:
#            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' % (user.nickname(), users.create_logout_url('/')))
#        else:
#            greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))
#        self.response.out.write('<html><body>%s</body></html>' % greeting)



    #    user = users.get_current_user()
    #    self.response.write(user)
    #    if user:
    #        url = users.create_logout_url(self.request.uri)
    #        url_linktext = 'Logout'
    #    else:
    #        url = users.create_login_url(self.request.uri)
    #        url_linktext = 'Login'

    #    template_values = {
    #        'user': user,
    #        'greetings': greetings,
    #        'guestbook_name': urllib.quote_plus(guestbook_name),
    #        'url': url,
    #        'url_linktext': url_linktext,
    #    }

    #    template = JINJA_ENVIRONMENT.get_template('index.html')
    #    self.response.write(template.render(template_values))

#class Guestbook(webapp2.RequestHandler):
#    def post(self):
        # We set the same parent key on the 'Greeting' to ensure each
        # Greeting is in the same entity group. Queries across the
        # single entity group will be consistent. However, the write
        # rate to a single entity group should be limited to
        # ~1/second.
#        guestbook_name = self.request.get('guestbook_name',
#                                          DEFAULT_GUESTBOOK_NAME)
#        greeting = Greeting(parent=guestbook_key(guestbook_name))

#        if users.get_current_user():
#            greeting.author = Author(
#                    identity=users.get_current_user().user_id(),
#                    email=users.get_current_user().email())

#        greeting.content = self.request.get('content')
#        greeting.put()

#        query_params = {'guestbook_name': guestbook_name}
#        self.redirect('/?' + urllib.urlencode(query_params))

######################################################################################################################################


class MyHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            k=user.nickname()
            if k in allowed_users:
                greeting = ('Welcome, %s!<a href="/NewEntry"> <br><br><br>Go For Data Entry</a> <br><br>(<a href="%s">google sign out</a>)' %
                            (user.nickname(),users.create_logout_url('/')))
            else:
                greeting = ('Welcome, You are not allowed to do data entry, try with nirma account ! (<a href="%s">sign out</a>)' %
                            (users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))

        self.response.out.write('<html><body>%s</body></html>' % greeting)



###################################################################################################################
class NewEntry(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            k=user.nickname()
            if k in allowed_users:
                template = JINJA_ENVIRONMENT.get_template('main.html')
                self.response.write(template.render())
            else:
                greeting=('Welcome, You are not allowed to do data entry, try with nirma account ! (<a href="%s">sign out</a>)' %
                            (users.create_logout_url('/NewEntry')))
                self.response.out.write('<html><body>%s</body></html>' % greeting)
        else:
            greeting = ('<a href="%s">Sign in or register</a>.' %
                        users.create_login_url('/'))
            self.response.out.write('<html><body>%s</body></html>' % greeting)

class Conformation(webapp2.RequestHandler):
    def get(self):self.response.write("oops - worng page")
    def post(self):
        #self.response.write("hhhhhhs")
        regid=self.request.get('regid')
        name=self.request.get('name')
        contactnum=self.request.get('contactnum')
        email=self.request.get('email')
        totalfee=self.request.get('totalfee')
        paid=self.request.get('paid')
        remaining=self.request.get('remaining')
        EVENTS=self.request.get_all('EVENTS')
        WORKSHOPS=self.request.get_all('WORKSHOPS')
        TUTORIALS=self.request.get_all('TUTORIALS')
        template_values={
            'regid' : regid,
            'name': name,
            'contactnum': contactnum,
            'email':email,
            'totalfee': totalfee,
            'paid': paid,
            'remaining': remaining,
            'EVENTS': EVENTS,
            'WORKSHOPS': WORKSHOPS,
            'TUTORIALS': TUTORIALS,
        }
        #self.response.write(self.request)
        template = JINJA_ENVIRONMENT.get_template('conformation.html')
        self.response.write(template.render(template_values))


class FormData(ndb.Model):
    """Data Entry For Fest"""
    regid = ndb.StringProperty()
    name = ndb.StringProperty()
    contactnum = ndb.StringProperty()
    email = ndb.StringProperty()
    totalfee = ndb.IntegerProperty()
    paid = ndb.IntegerProperty()
    remaining = ndb.IntegerProperty()
    EVENTS = ndb.StringProperty()
    WORKSHOPS = ndb.StringProperty()
    TUTORIALS = ndb.StringProperty()
    volunteer = ndb.StringProperty()

class SubmitNuForm(webapp2.RequestHandler):
    def get(self):
        self.response.write("ooops - wrong-page")

    def post(self):
        n=self.request.get('name')
        d=FormData()
        d.regid=self.request.get('regid')
        d.name=n
        d.contactnum=self.request.get('contactnum')
        d.email=self.request.get('email')
        d.totalfee=int(self.request.get('totalfee'))
        d.paid=int(self.request.get('paid'))
        d.remaining=int(self.request.get('remaining'))
        EVENTS=""
        c=self.request.get_all('EVENTS')
        for x in c: EVENTS=EVENTS+x+", "
        d.EVENTS=EVENTS
        c=self.request.get_all('WORKSHOPS')
        WORKSHOPS=""
        for x in c: WORKSHOPS=WORKSHOPS+x+", "
        d.WORKSHOPS=WORKSHOPS
        TUTORIALS=""
        c=self.request.get_all('TUTORIALS')
        for x in c: TUTORIALS=TUTORIALS+x+", "
        d.TUTORIALS=TUTORIALS
        u=users.get_current_user()
        d.volunteer=u.email()
        k=d.put()
        template_values={'key': k,}
        template = JINJA_ENVIRONMENT.get_template('submitted.html')
        self.response.write(template.render(template_values))


###############################################################################################################

class ShowAll(webapp2.RequestHandler):
	def get(self):
		participants_query=FormData.query()
		participants=participants_query.fetch()
#		self.response.write("hello from showAll")
		template_values={'participants': participants }
		template = JINJA_ENVIRONMENT.get_template('showall.html')
		self.response.write(template.render(template_values))
#        self.response.write(template.render(template_values))

	def post(self):
		self.response.write("Helllllo, wrong page... nothing to do here !!")


app = webapp2.WSGIApplication([
    ('/', MyHandler),
	('/NewEntry', NewEntry),
	('/Conformation', Conformation),
	('/Submit',SubmitNuForm),
	('/ShowAll',ShowAll),
], debug=True)
