import re
from model.contact import Contact


def test_fields_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_database = sorted(db.get_detail_contact_list(), key=Contact.id_or_max)
    assert_lists(contact_from_home_page, contact_from_database)

def assert_lists(list1, list2):
    if len(list1) == len(list2):
        for i in range(len(list1)):
            assert list1[i].lastname == list2[i].lastname
            assert list1[i].firstname == list2[i].firstname
            assert list1[i].address == list2[i].address
            assert list1[i].all_emails == merge_emails(list2[i])
            assert list1[i].all_phones == merge_phones(list2[i])

def clear(s):
    return re.sub("[() -]]", "", s)

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
