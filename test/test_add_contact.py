# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="fname vfrr", middlename="mname fsdf", lastname="lname sdf",
                               nickname="nname sd", title="titledfs", company="companysdfsf",
                               address="addresshk kjksdf jkjkf kjfkasjf kk353kh", homephone="43544565",
                               mobilephone="45678", workphone="45688", fax="46578", email="email1afsfds",
                               email2="email2asfas", email3="email3dfdaf", homepage="homepagezddfsfsf",
                               bday="4", bmonth="April", byear="1950", aday="2", amonth="August", ayear="2000",
                               address2="secaddress dsfdsfasf", phone2="sechome dfsdgf",
                               notes="secnotes sdfjskf skjfkasfj iajsfksddjfkasf kfjsd kfasjf"))
    app.session.logout()
