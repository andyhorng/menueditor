# encoding: utf-8
from google.appengine.ext import ndb


class Menu(ndb.Model):
    name = ndb.StringProperty()
    address = ndb.StringProperty()
    area = ndb.StringProperty()
    shippments = ndb.StringProperty(repeated=True)
    min_amount = ndb.IntegerProperty() # 最小外送金額
    tel = ndb.StringProperty()
    items = ndb.JsonProperty()

    def to_dict(self):
        rt = ndb.Model.to_dict(self)
        rt['id'] = self.key.id()

        return rt
