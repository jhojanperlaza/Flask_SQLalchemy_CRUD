from app import app
from utils.db import db

with app.app_context():
    """ Create the Tables when start web aplication"""
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
