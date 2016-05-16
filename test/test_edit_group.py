# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name1", header="header1", footer="footer1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edited_group = Group(name="name_edited", header="header_edited", footer="footer_edited")
    app.group.edit_group_by_id(group.id, edited_group)
    new_groups = db.get_group_list()
    for gr in old_groups:
        if gr.id == group.id:
            gr = edited_group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
