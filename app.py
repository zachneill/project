from flask import Flask, render_template
from peewee import *

db = SqliteDatabase('YOUR_DATABASE.db')

class BaseModel(Model):
    class Meta:
        database = db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
