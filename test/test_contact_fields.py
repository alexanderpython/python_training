import re

def test_fields_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.telephone == clear(contact_from_edit_page.telephone)
    assert contact_from_home_page.email == clear(contact_from_edit_page.email)

def clear(s):
    return re.sub("[() -]]", "", s)
