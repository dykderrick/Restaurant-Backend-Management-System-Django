from mongoengine import *


class Discount(EmbeddedDocument):
    type = StringField()
    amount = FloatField()


class PromoCode(Document):
    code = StringField()
    description = StringField()
    validStart = DateField()
    validEnd = DateField()
    discount = EmbeddedDocumentField(Discount)
    _partitionKey = StringField()

    meta = {'collection': 'promocode'}
