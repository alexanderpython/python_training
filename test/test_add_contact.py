# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="test_firstname", lastname="test_lastname",
                                            address="test_address", telephone="test_telephone", email="test_email"))
    app.session.logout()



