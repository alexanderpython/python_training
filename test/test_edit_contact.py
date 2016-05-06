# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="lastname1", firstname="firstname1", address="address1",
                                   email="email1", telephone="telephone1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="lastname_edited", firstname="firstname_edited", address="address_edited",
                      email="email_edited", telephone="telephone_edited")
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.key) == sorted(new_contacts, key=Contact.key)
