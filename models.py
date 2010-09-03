from google.appengine.ext import db

class Corridors(db.Model):
  markers = db.TextProperty()
  routes = db.TextProperty()
  comments = db.TextProperty()
  circulator = db.StringProperty(multiline=False)
  commute = db.StringProperty(multiline=False)
  email = db.StringProperty(multiline=False)
  date = db.DateTimeProperty(auto_now_add=True)
  batch = db.StringProperty(multiline=False, default="New")  


class Routes(db.Model):
  markers = db.TextProperty()
  routes = db.TextProperty()
  busstops = db.TextProperty()
  comments = db.TextProperty()
  circulator = db.StringProperty(multiline=False)
  commute = db.StringProperty(multiline=False)
  email = db.StringProperty(multiline=False)
  date = db.DateTimeProperty(auto_now_add=True)
  batch = db.StringProperty(multiline=False, default="New")  

