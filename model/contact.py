from sys import maxsize


class Contact:

    def __init__(self, lastname=None, firstname=None, id=None, address=None, telephone=None, telephone2=None,
                 telephone3=None, email=None, email2=None, email3=None, all_phones=None, all_emails=None):
        self.lastname = lastname
        self.firstname = firstname
        self.id = id
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.telephone = telephone
        self.telephone2 = telephone2
        self.telephone3 = telephone3
        self.all_phones = all_phones
        self.all_emails = all_emails

    def __repr__(self):
        return "%s:%s:%s" % (self.lastname, self.firstname, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def key(self):
        return self.lastname
