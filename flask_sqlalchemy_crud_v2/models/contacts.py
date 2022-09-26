from utils.db import db

class Contact(db.Model):
    """ Class that creates a new contact"""
    __tablename__ = 'Contact'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    cell = db.Column(db.String(100))

    def __init__(self, fullname, email, cell):
        self.fullname = fullname
        self.email = email
        self.cell = cell
