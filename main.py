from app import app, db
from database.setup_database import *
# from auth import *
# from admin import admin
# from api import api
# from models import *
# from views import *
# admin.setup()
# api.setup()

setup = setup_db('x01.db')

if __name__ == '__main__':
    app.run(host="localhost", port=81)
