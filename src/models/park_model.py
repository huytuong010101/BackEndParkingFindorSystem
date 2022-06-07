from peewee import *
from database.connection import db
from models import Node
import datetime


class Park(Model):
    id = AutoField()
    park_name = CharField(null=False)
    address = TextField(null=True)
    long = FloatField(null=True)
    lat = FloatField(null=True)
    open_time = TimeField(null=True)
    close_time = TimeField(null=True)
    node = ForeignKeyField(Node, on_delete="CASCADE")
    disable_at = DateTimeField(null=True)
    price = IntegerField(default=0, null=False)

    class Meta:
        database = db
