import sqlite3
from peewee import *
db = SqliteDatabase('x01.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

def setup_db(database):
    conn = sqlite3.connect(database)
    with db:
        db.create_tables([User])
