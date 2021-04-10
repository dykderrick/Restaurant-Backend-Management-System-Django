from mongoengine import *


class Table(Document):
    capacity = IntField()
    tableNo = StringField()
    status = StringField()
    _partitionKey = StringField()

    meta = {
        'collection': 'tables',
    }
