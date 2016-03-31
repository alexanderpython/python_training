# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname",
                       address="test_address", telephone="test_telephone", email="test_email"))
    app.session.logout()



