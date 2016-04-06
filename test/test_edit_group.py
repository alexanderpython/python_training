# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    app.group.edit_first_group(Group(name="131", header="12313", footer="1231231231231131"))
