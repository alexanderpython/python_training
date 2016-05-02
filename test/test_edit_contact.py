# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test", address="test", telephone="test", email="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="test_firstname_new", lastname="test_lastname_new",
            address="test_address_new", telephone="test_telephone_new",
            email="test_email_new")
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.email) == sorted(new_contacts, key=Contact.email)
