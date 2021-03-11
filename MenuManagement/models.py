from mongoengine import *

connect('my-db', host='mongodb+srv://admin:Dings0551@restaurant-db.9zain.mongodb.net/my-db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')


class Dish(Document):
    name = StringField()
    description = StringField()
    price = FloatField()
    category = StringField()
    dishID = StringField()
    ETP = IntField()  # Estimated Time of Preparation
    _partitionKey = StringField()

    meta = {'collection': 'dishes'}
