from application import db
from datetime import datetime

class Slides(db.Model):
    slideID = db.Column(db.Integer, primary_key=True)
    slideTitle = db.Column(db.String(50))
    slideRow = db.Column(db.String(300))
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.slideID), '\r\n',
            'Email: ', self.slideTitle, '\r\n',
            'Name: ', self.slideRow, ' '])

        def __repr__(self):
            return ''.join(['UserID: ', str(self.slideID), '\r\n',
            'Email: ', self.slideTitle])
