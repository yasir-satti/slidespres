from application import db
from application.models import Slides

db.drop_all()
db.create_all()