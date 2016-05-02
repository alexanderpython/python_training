from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, telephone=None, email=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.telephone = telephone
        self.email = email

    def __repr__(self):
        return "%s" % self.email

    def __eq__(self, other):
        return self.email == other.email

    def email(self):
        return self.email
