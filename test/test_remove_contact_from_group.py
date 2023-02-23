import random
from model.contact import Contact
from model.group import Group


def test_remove_contact_from_group(app, orm):
    db = orm
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(db.get_group_list())

    if (len(db.get_contacts_in_group(group))) == 0:
        if len(db.get_contacts_not_in_group(group)) == 0:
            app.contact.create(Contact(firstname="scsc", middlename="afe", lastname="rtrt", nickname="bbbb",
                                       address="irjfri 12!^:kjff kjekdj", homephone="+435-44-565",
                                       mobilephone="(456)78",
                                       workphone="45688", fax="46578", email="email1-s_fds@test.test",
                                       email3="ema.il3daf",
                                       address2="secaddress dsfdsfasf", secondaryphone="sechome dfsdgf"))
        c = random.choice(db.get_contacts_not_in_group(group))
        app.contact.add_contact_to_group(c, group)

    old_contacts_in_group = db.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.remove_contact_from_group(contact, group)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
