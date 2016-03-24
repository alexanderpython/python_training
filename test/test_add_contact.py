# -*- coding: utf-8 -*-
import unittest

from fixture.application import Application
from model.contact import Contact
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.contact.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="test_firstname", lastname="test_lastname",
                               address="test_address", telephone="test_telephone", email="test_email"))
    app.contact.session.logout()