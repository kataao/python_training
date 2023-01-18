from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="sssss", middlename="ddddd", lastname="ffffff", nickname="ggggg",
                                             title="hhhhh", company="kkkkkkk", address="", homephone="", mobilephone="",
                                             workphone="", fax="", email="", email2="", email3="", homepage="",
                                             bday="5", bmonth="May", byear="2001", aday="6", amonth="June",
                                             ayear="2002", address2="", phone2="", notes=""))
