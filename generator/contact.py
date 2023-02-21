from model.contact import Contact
import jsonpickle
import os.path
import random
import string
import getopt
import sys


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
    return prefix + ''.join([random.choice(symbols) for _ in range(random.randrange(maxlen))])


def random_day():
    return str(random.randrange(1, 29))


def random_year():
    return str(random.randrange(1940, 2020))


def random_month():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"])


testdata = [Contact(firstname="", lastname="", address="")] + [
    Contact(firstname=random_string("fname", 15), middlename=random_string("mname", 15),
            lastname=random_string("lname", 15), nickname=random_string("nname", 15), title=random_string("ttl", 5),
            company=random_string("cmp", 10), address=random_string("addr", 50), homephone=random_string("", 10),
            mobilephone=random_string("", 10), workphone=random_string("", 10), fax=random_string("", 10),
            email=random_string("", 15), email2=random_string("", 15), email3=random_string("", 15),
            homepage=random_string("", 15), bday=random_day(), bmonth=random_month(), byear=random_year(),
            aday=random_day(), amonth=random_month(), ayear=random_year(), address2=random_string("", 50),
            secondaryphone=random_string("", 10), notes=random_string("", 100))
    for _ in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
