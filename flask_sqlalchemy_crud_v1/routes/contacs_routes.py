from crypt import methods
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contacts import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def main():
    """ get all contacts"""
    all_contacs = Contact.query.all()

    return render_template('index.html', all_contacts=all_contacs)

@contacts.route('/new', methods=['POST'])
def new_contact():
    """ instantiate new contact"""
    name = request.form['fullname']
    email = request.form['email']
    cell = request.form['cell']
    new_instance_contact = Contact(name, email, cell)

    """ save new instance contact in database """
    db.session.add(new_instance_contact)
    db.session.commit()

    flash("contact created successfully!!")
    return redirect('/')

@contacts.route('/update/<id>', methods = ['POST', 'GET'])
def update_contact(id):
    contact_to_update = Contact.query.get(id)

    if request.method == 'POST':
        contact_to_update.fullname = request.form['fullname']
        contact_to_update.email = request.form['email']
        contact_to_update.cell = request.form['cell']

        db.session.commit()
        flash("contact updated successfully!!")
        return redirect(url_for('contacts.main'))

    else:
        return render_template('update.html', contact=contact_to_update)

@contacts.route('/delete/<id>')
def delete_contact(id):
    contact_to_delete = Contact.query.get(id)

    """ Delete a contact of database"""
    db.session.delete(contact_to_delete)
    db.session.commit()

    flash("contact deleted successfully!!")
    return redirect('/')
