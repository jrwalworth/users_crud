from flask import render_template, request, redirect
from app.models.user import User
from app import app

#root route
@app.route('/')
def index():
    return redirect('/users')

#All Users page
@app.route('/users')
def all_users():
    users = User.get_all()
    print(users)
    return render_template('index.html', all_users=users)

#Page to add new user
@app.route('/users/new')
def new():
    return render_template('new.html')

#DB method to add user and redirect to All Users
@app.route('/users/add', methods=["POST"])
def add_user():
    data = {
        "fname" : request.form["fname"], 
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/users')

#Show single user
@app.route('/users/<int:id>/show')
def show_user(id):
    data = {
        "id": id,
    }
    user = User.get_one(data)
    return render_template('show_user.html', one_user=user)

#Edit user page
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        "id": id,
    }
    #User.update(data)
    user = User.get_one(data)
    return render_template('edit_user.html', e_user=user)

#Update user in DB
@app.route('/users/<int:id>/update', methods=['POST'])
def update_db(id):
    data = {
        "id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    User.update(data)
    #must use f string if you pass in a parameter to redirect.
    return redirect(f'/users/{id}/show')

#Delete user
@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        "id": id,
    }
    User.delete(data)
    return redirect('/users')


