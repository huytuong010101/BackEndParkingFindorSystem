from peewee import *
from database.connection import db
from models import Node

class Park(Model):
    id = AutoField()
    park_name = CharField(null=False)
    address = TextField(null=True)
    long = FloatField(null=True)
    lat = FloatField(null=True)
    open_close = TimeField(null=True)
    close_time = TimeField(null=True)
    node = ForeignKeyField(Node, on_delete="CASCADE")

    class Meta:
        database = db
        