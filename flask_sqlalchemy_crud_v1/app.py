"""
creation and configuration of the web application
"""
from flask import Flask
from routes.contacs_routes import contacts
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secret_key"
""" configuration of database connection"""
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mypass@localhost/db_contacts"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(contacts)

if __name__ == "__main__":
    app.run(debug=True)
