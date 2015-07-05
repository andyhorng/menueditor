# encoding: utf-8
from google.appengine.ext import ndb


class Menu(ndb.Model):
    name = ndb.StringProperty()
    area = ndb.StringProperty()
    address = ndb.StringProperty()
    shippments = ndb.StringProperty(repeated=True)
    min_amount = ndb.IntegerProperty(default=0) # 最小外送金額
    tel = ndb.StringProperty()
    items = ndb.JsonProperty(default=[])
    business_hours = ndb.JsonProperty(default=[])
    addresses = ndb.JsonProperty(default=[])

    def to_dict(self):
        rt = ndb.Model.to_dict(self)
        rt['id'] = self.key.id()

        return rt
