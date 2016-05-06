from sys import maxsize


class Contact:

    def __init__(self, lastname=None, firstname=None, address=None, email=None, telephone=None, id=None):
        self.lastname = lastname
        self.firstname = firstname
        self.address = address
        self.email = email
        self.telephone = telephone
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.lastname, self.firstname, self.address, self.email, self.telephone, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def key(self):
        return self.lastname
