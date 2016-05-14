import json
import getopt
import sys
import os
from model.contact import Contact
import random
import string


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone():
    symbols = string.digits
    return "79" + "".join([random.choice(symbols) for i in range(9)])

testdata = [Contact(lastname="", firstname="", address="", email="", telephone="")] + [
    Contact(lastname=random_string("lname", 10), firstname=random_string("fname", 10),
            address=random_string("address", 15), email=random_string("email", 15), telephone=random_phone()
            )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
