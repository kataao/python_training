from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(firstname="sssss", middlename="ddddd", lastname="ffffff", nickname="ggggg",
                                           title="hhhhh", company="kkkkkkk", address="", homephone="", mobilephone="",
                                           workphone="", fax="", email="", email2="", email3="", homepage="", bday="5",
                                           bmonth="May", byear="2001", aday="6", amonth="June", ayear="2002",
                                           address2="", phone2="", notes=""))
