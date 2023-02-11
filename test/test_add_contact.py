# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fname vfrr", middlename="mname fsdf", lastname="lname sdf", nickname="nname sd",
                      title="titledfs", company="companysdfsf", address="addresshk kjksdf jkjkf kjfkasjf kk353kh",
                      homephone="43544565", mobilephone="45678", workphone="45688", fax="46578", email="email1afsfds",
                      email2="email2asfas", email3="email3dfdaf", homepage="homepagezddfsfsf", bday="4", bmonth="April",
                      byear="1950", aday="2", amonth="August", ayear="2000", address2="secaddress dsfdsfasf",
                      phone2="sechome dfsdgf", notes="secnotes sdfjskf skjfkasfj iajsfksddjfkasf kfjsd kfasjf")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
