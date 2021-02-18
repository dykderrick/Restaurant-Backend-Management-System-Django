from mongoengine import *

connect('my-db', host='mongodb+srv://admin:Dings0551@restaurant-db.9zain.mongodb.net/my-db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')


class DishContent(EmbeddedDocument):
    dishID = StringField()
    amount = IntField()
    status = StringField()


class Customer(EmbeddedDocument):
    name = StringField()
    quantity = IntField()
    membershipID = StringField()


class Order(Document):
    createdTime = DateTimeField()
    tableNo = StringField()
    dishes = ListField(EmbeddedDocumentField(DishContent))
    diningOption = StringField()
    isFinished = BooleanField()
    customerInfo = EmbeddedDocumentField(Customer)

    meta = {'collection': 'orders'}
