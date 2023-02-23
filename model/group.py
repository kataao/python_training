from sys import maxsize


class Group:
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "Group(%s, %s, %s, %s)" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def update(self, other):
        if other.name is not None:
            self.name = other.name
        if other.name is not None:
            self.header = other.header
        if other.name is not None:
            self.footer = other.footer
        if other.id is not None:
            self.id = other.id
