# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone():
    symbols = string.digits
    return "79" + "".join([random.choice(symbols) for i in range(9)])

testdata = [Contact(firstname="", lastname="", address="", telephone="", email="")] + [
    Contact(firstname=random_string("fname", 10), lastname=random_string("lname", 10),
            address=random_string("address", 20), telephone=random_phone(), email=random_string("email", 20)
            )
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.email) == sorted(new_contacts, key=Contact.email)
