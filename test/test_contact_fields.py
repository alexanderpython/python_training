import re

def test_fields_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails == merge_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones == merge_phones(contact_from_edit_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                         map(lambda x: clear(x),
                             filter(lambda x: x is not None,
                                    [contact.telephone, contact.telephone2, contact.telephone3]))))

def merge_emails(contact):
    return "\n".join(filter(lambda x: x != "",
                         map(lambda x: clear(x),
                             filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))
