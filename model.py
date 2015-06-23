from google.appengine.ext import ndb


class Menu(ndb.Model):
    name = ndb.StringProperty()
    address = ndb.StringProperty()
    items = ndb.JsonProperty()

    def to_dict(self):
        return {"name":self.name,
                "address": self.address,
                "items": self.items,
                "id": self.key.id()}

    def update_from_dict(self, d):

        fields = ['name', 'address', 'items']

        for f in fields:
            setattr(self, f, d[f])
