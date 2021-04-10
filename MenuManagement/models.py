from mongoengine import *


class Dish(Document):
    name = StringField()
    description = StringField()
    price = FloatField()
    category = StringField()
    dishID = StringField()
    ETP = IntField()  # Estimated Time of Preparation
    _partitionKey = StringField()

    meta = {'collection': 'dishes'}
