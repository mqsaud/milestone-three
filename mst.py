import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


mst = Flask(__name__)

mst.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
mst.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mst.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(mst)


@mst.route("/")
# Home Page
@mst.route("/get_recipes")
def get_recipes():
    recipes = mongo.db.recipes.find()
    return render_template("recipes.html", recipes=recipes)


# Registeration Page
@mst.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check the availabilty of username
        new_user = mongo.db.users.find_one(
            {"username": request.form.get("user-name").lower()})

        if new_user:
            flash("Username already taken. Please use differnet Username.")
            return redirect(url_for("register"))

        register = {
            "firstname": request.form.get("fname").lower(),
            "surname": request.form.get("sname").lower(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("user-name").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("user-name").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


# Log In page
@mst.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Chick if the username exists in database?
        check_user = mongo.db.users.find_one(
            {"username": request.form.get("user-name").lower()})

        if check_user:
            # ensure the hash of newly supplied psaawoad is same as the hash of
            # stored password.
            if check_password_hash(
               check_user["password"], request.form.get("password")):
                session["user"] = request.form.get("user-name").lower()
                flash("Welcom, {}".format(request.form.get("user-name")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username or Password")
                return redirect(url_for("login"))

        else:
            # username does not rxists
            flash("Incorrect Username or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@mst.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's name from database
    username = mongo.db.users.find_one(
              {"username": session["user"]})["username"]
    return render_template("profile.html", username=username)


if __name__ == "__main__":
    mst.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
