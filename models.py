from google.appengine.ext import ndb
from webapp2_extras import sessions
from webapp2_extras import auth

import logging
import os.path
import webapp2

class journal(ndb.Model):
    #My Journal
    jText = ndb.StringProperty()
    author = ndb.StringProperty()
    jRate = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    
class free(ndb.Model):
    #My Free Writing
    fTitle =ndb.StringProperty()
    fText = ndb.StringProperty()
    author = ndb.StringProperty()
    fRate = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)