from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email=None, email2=None,
                 email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 address2=None, secondaryphone=None, notes=None, id=None, all_phones_from_home_page=None,
                 all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "Contact(%s, %s, %s)" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def update(self, other):
        if other.firstname is not None:
            self.firstname = other.firstname
        if other.middlename is not None:
            self.middlename = other.middlename
        if other.lastname is not None:
            self.lastname = other.lastname
        if other.nickname is not None:
            self.nickname = other.nickname
        if other.title is not None:
            self.title = other.title
        if other.company is not None:
            self.company = other.company
        if other.address is not None:
            self.address = other.address
        if other.homephone is not None:
            self.homephone = other.homephone
        if other.mobilephone is not None:
            self.mobilephone = other.mobilephone
        if other.workphone is not None:
            self.workphone = other.workphone
        if other.fax is not None:
            self.fax = other.fax
        if other.email is not None:
            self.email = other.email
        if other.email2 is not None:
            self.email2 = other.email2
        if other.email3 is not None:
            self.email3 = other.email3
        if other.homepage is not None:
            self.homepage = other.homepage
        if other.bday is not None:
            self.bday = other.bday
        if other.bmonth is not None:
            self.bmonth = other.bmonth
        if other.byear is not None:
            self.byear = other.byear
        if other.aday is not None:
            self.aday = other.aday
        if other.amonth is not None:
            self.amonth = other.amonth
        if other.ayear is not None:
            self.ayear = other.ayear
        if other.address2 is not None:
            self.address2 = other.address2
        if other.secondaryphone is not None:
            self.secondaryphone = other.secondaryphone
        if other.notes is not None:
            self.notes = other.notes
        if other.id is not None:
            self.id = other.id
