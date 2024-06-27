from flask import render_template,request
from app import app
from model.user_model import user_model

obj = user_model()

@app.route('/user')
def user():
    data = obj.get_all_user()
    return render_template('index.html', data=data)

@app.route('/add_user', methods=['POST'])
def add_user():
    return obj.add_user(request.form)

@app.route('/update_user', methods=['PUT'])
def update_user():
    return obj.update_user(request.form)

@app.route('/delete_user/<id>', methods=['DELETE'])
def delete_user(id):
    return obj.delete_user(id)