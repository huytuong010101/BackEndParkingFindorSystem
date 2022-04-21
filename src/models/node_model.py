from peewee import *
from database.connection import db


class Node(Model):
    id = AutoField()
    node_name = CharField(null=False)
    address = TextField(null=True)
    token = CharField(null=True)
    long = FloatField(null=True)
    lat = FloatField(null=True)

    class Meta:
        database = db
