# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random


def test_add_contact(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="lastname1", firstname="firstname1", address="address1", email="email1",
                                   telephone="telephone1"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    groups = orm.get_group_list()
    group = random.choice(groups)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
