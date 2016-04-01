# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="test_firstname_new", lastname="test_lastname_new",
                                           address="test_address_new", telephone="test_telephone_new",
                                           email="test_email_new"))
