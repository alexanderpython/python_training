from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, telephone=None, email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.telephone = telephone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.firstname, self.lastname, self.address, self.telephone, self.email, self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
