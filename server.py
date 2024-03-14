from flask_app import app
from flask_app.controllers import recipe_controller
# from flask_app.config.db_connection import connectToDb


if __name__ == "__main__":
    # connectToDb()
    app.run(host= '127.0.0.1', debug=True)