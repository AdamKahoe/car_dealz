from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Car:
    db_name = 'car_deal_schema'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.model = db_data['model']
        self.make = db_data['make']
        self.description = db_data['description']
        self.price = db_data['price']
        self.year = db_data['year']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user_id = db_data['user_id']
        self.user = ""

    @classmethod
    def save(cls,data):
        query = "INSERT INTO cars (model, make, description, price, year, user_id) VALUES (%(model)s,%(make)s,%(description)s,%(price)s,%(year)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_cars = []
        for row in results:
            print(row['id'])
            all_cars.append( cls(row) )
        return all_cars

                ###### JOIN ATTEMPT

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM cars JOIN users ON cars.user_id = users.id WHERE cars.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)

        car = cls(results[0])
        car.user = results[0]['first_name']
        # car.user = results[0]['last_name']
        return car

    @classmethod
    def update(cls, data):
        query = "UPDATE cars SET model=%(model)s, make=%(make)s, description=%(description)s, price=%(price)s, year=%(year)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)


    @staticmethod
    def validate_car(car):
        is_valid = True
        if len(car['model']) < 1:
            is_valid = False
            flash("Model must be at least 1 character", "car")
        if len(car['make']) < 1:
            is_valid = False
            flash("Make must be at least 1 character","car")
        if len(car['description']) < 1:
            is_valid = False
            flash("Description must be at least 1 character","car")
        if len(car['price']) > 0:
            is_valid = False
            flash("Price must greater than 0", "car")
        if len(car['year']) > 0:
            is_valid = False
            flash("Year must be greater than 0", "car")
        return is_valid