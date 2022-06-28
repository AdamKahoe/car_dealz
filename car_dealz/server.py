from flask_app import app

from flask_app.controllers import controllers_users, controllers_cars
from flask_app.models import models_car, models_user

if __name__=="__main__":
    app.run(debug=True)