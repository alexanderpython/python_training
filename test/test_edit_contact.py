# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="lastname1", firstname="firstname1", address="address1",
                                   email="email1", telephone="telephone1"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    edited_contact = Contact(lastname="lastname_edited", firstname="firstname_edited", address="address_edited",
                      email="email_edited", telephone="telephone_edited")
    app.contact.edit_contact_by_id(contact.id, edited_contact)
    new_contacts = db.get_contact_list()
    for cont in old_contacts:
        if cont.id == contact.id:
            cont.firstname = edited_contact.firstname
            cont.lastname = edited_contact.lastname
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
