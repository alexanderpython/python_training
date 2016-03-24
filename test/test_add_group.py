# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.group.session.login(username="admin", password="secret")
    app.group.create(Group(name="fghf", header="fhfhffhfg", footer="fghfhfhfhf"))
    app.group.session.logout()

def test_add_empty_group(app):
    app.group.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.group.session.logout()