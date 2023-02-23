import random
from model.contact import Contact


def test_modify_first_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    contact = Contact(firstname="sssss", middlename="ddddd", lastname="ffffff", nickname="ggggg", title="hhhhh",
                      company="kkkkkkk", address="", homephone="", mobilephone="", workphone="", fax="", email="",
                      email2="", email3="", homepage="", bday="5", bmonth="May", byear="2001", aday="6", amonth="June",
                      ayear="2002", address2="", secondaryphone="", notes="", id=old_contact.id)
    app.contact.modify_contact_by_id(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contact.update(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
