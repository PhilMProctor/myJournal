
from google.appengine.ext import ndb
from google.appengine.api import users

import jinja2
import logging
import os.path
import webapp2
import time
import datetime
import sys
import urllib

from webapp2_extras import auth
from webapp2_extras import sessions
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

from webapp2_extras.auth import InvalidAuthIdError
from webapp2_extras.auth import InvalidPasswordError

from models import journal

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'views')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
  
class BaseHandler(webapp2.RequestHandler):
  @webapp2.cached_property
  def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

  def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))
        
class MainPage(BaseHandler):

  def get(self):
        user = users.get_current_user()

        if user:
          entries = journal.query()
          daystamp=datetime.datetime.strftime((datetime.datetime.now()),'%Y-%m-%d')
          datestamp=datetime.datetime.strftime((datetime.datetime.now()),'%Y-%m-%d %H:%M')
          params = {
                  'entries': entries,
                  'nickname': user.nickname(),
                  'daystamp': daystamp,
                  'datestamp': datestamp}
        
          self.render_template('home.html', params)
        else:
          self.redirect(users.create_login_url(self.request.uri))
            
        



app = webapp2.WSGIApplication([
        ('/', MainPage)
        ],
        debug=True)