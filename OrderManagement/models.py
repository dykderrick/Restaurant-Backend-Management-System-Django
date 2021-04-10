from mongoengine import *


class DishContent(EmbeddedDocument):
    dishID = StringField()
    amount = IntField()
    status = StringField()


class Customer(EmbeddedDocument):
    name = StringField()
    quantity = IntField()
    username = StringField()


class Order(Document):
    createdTime = DateTimeField()
    tableNo = StringField()
    dishes = ListField(EmbeddedDocumentField(DishContent))
    diningOption = StringField()
    isFinished = BooleanField()
    customerInfo = EmbeddedDocumentField(Customer)
    _partitionKey = StringField()

    meta = {'collection': 'orders'}
