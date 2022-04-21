from peewee import *
from database.connection import db
from models import Park


class ParkRecord(Model):
    id = AutoField()
    park = ForeignKeyField(Park, on_delete="CASCADE")
    time = DateTimeField()
    image = CharField(null=False)
    num_of_empty_space = IntegerField(null=False)

    class Meta:
        database = db
