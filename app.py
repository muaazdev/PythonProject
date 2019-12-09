from flask import Flask, render_template, request
import random
import string

import os
project_dir = os.path.dirname(os.path.abspath(__file__))
myapp = Flask(__name__)

print(project_dir)

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "school.db"))

myapp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myapp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(myapp)

#db.create_all()


class User(db.Model):

    name = db.Column(db.String(40), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(40), unique=False, nullable=False)
    role = db.Column(db.String(10), unique=False, nullable=False)


#db.create_all()


@myapp.route('/users', methods=["POST", "GET"])
def users():
      #print(request.form['name'])


    if request.method == "POST":
        user = User()
        user.name = request.form['name']
        user.role = request.form.get('role')

        ran = 8
        letters = string.ascii_lowercase
        pas = ''.join(random.choice(letters) for i in range(ran))
        user.password = pas

        db.session.add(user)
        db.session.commit()

    return render_template("users.html")


@myapp.route('/')
def home():

    return render_template("/home.html")


@myapp.route('/viewdata')
def viewdata():

    return render_template("/viewdata.html")


if __name__ == "__main__":
    myapp.run(debug=True)
