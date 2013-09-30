from google.appengine.ext import ndb
from webapp2_extras import sessions
from webapp2_extras import auth

import logging
import os.path
import webapp2

class journal(ndb.Model):
    #My Journal
    jTitle = ndb.StringProperty()
    jContent = ndb.StringProperty()
    author = ndb.StringProperty()
    jRate = ndb.StringProperty()
    jPicture = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)