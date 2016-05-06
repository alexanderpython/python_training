# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="name_edited", header="header_edited", footer="footer_edited")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
