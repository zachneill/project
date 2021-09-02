from app import app, db
# from auth import *
# from admin import admin
# from api import api
# from models import *
# from views import *
# admin.setup()
# api.setup()

def create_tables():
    # Create table for each model if it does not exist.
    # Use the underlying peewee database object instead of the
    # flask-peewee database wrapper:
    db.database.create_tables([User], safe=True)

if __name__ == '__main__':
    # create_tables()
    app.run(host="localhost", port=80)
