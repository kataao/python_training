# -*- coding: utf-8 -*-
import re
import string
import random
import pytest

from model.contact import Contact


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
    for _ in range(5)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
