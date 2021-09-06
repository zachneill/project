from flask import Flask, render_template
from peewee import *

db = SqliteDatabase('database.db')
app = Flask(__name__)

@app.before_request
def _db_connect():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

@app.after_request
def after_request(response):
    db.close()
    return response

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
