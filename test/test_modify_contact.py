from random import randrange
from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="sssss", middlename="ddddd", lastname="ffffff", nickname="ggggg", title="hhhhh",
                      company="kkkkkkk", address="", homephone="", mobilephone="", workphone="", fax="", email="",
                      email2="", email3="", homepage="", bday="5", bmonth="May", byear="2001", aday="6", amonth="June",
                      ayear="2002", address2="", secondaryphone="", notes="")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
