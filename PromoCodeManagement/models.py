from mongoengine import *

connect('my-db', host='mongodb+srv://admin:Dings0551@restaurant-db.9zain.mongodb.net/my-db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')


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
