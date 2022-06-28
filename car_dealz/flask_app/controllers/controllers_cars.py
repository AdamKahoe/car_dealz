from pyexpat import model
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.controllers.controllers_users import dashboard
from flask_app.models.models_car import Car
from flask_app.models.models_user import User

@app.route('/new/car')
def new_car():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('add_car.html',user=User.get_by_id(data))


@app.route('/create/car',methods=['POST'])
def create_car():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Car.validate_car(request.form):
        return redirect('/new/car')
    data = {
        "model": request.form['model'],
        "make": request.form["make"],
        "description": request.form["description"],
        "price": request.form["price"],
        "year": request.form['year'],
        "user_id": session["user_id"]
    }
    Car.save(data)
    return redirect('/dashboard')

@app.route('/edit/car/<int:id>')
def edit_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_car.html",edit=Car.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/car/',methods=['POST'])
def update_car():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Car.validate_car(request.form):
        return redirect('/new/car')
    data = {
        "model": request.form['model'],
        "make": request.form['make'],
        "description": request.form['description'],
        "price": request.form['price'],
        "year": request.form['year'],
        "id": request.form['id']
    }
    Car.update(data)
    return redirect('/dashboard')

@app.route('/car/<int:id>')
def show_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_car.html",car=Car.get_one(data),user=User.get_by_id(user_data))

@app.route('/delete/car/<int:id>')
def delete_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Car.delete(data)
    return redirect('/dashboard')

@app.route('/purchase/car/')
def purchase_car(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Car.delete(data)
    return render_template("dashboard.html")