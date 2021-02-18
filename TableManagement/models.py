from mongoengine import *

connect('my-db', host='mongodb+srv://admin:Dings0551@restaurant-db.9zain.mongodb.net/my-db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE')


class Table(Document):
    capacity = IntField()
    tableNo = StringField()
    status = StringField()

    meta = {
        'collection': 'tables',
    }
