# -*- coding: utf-8 -*-
from application import Application
import unittest
import pytest
from group import Group

@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="fghf", header="fhfhffhfg", footer="fghfhfhfhf"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()