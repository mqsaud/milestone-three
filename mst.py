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
@mst.route("/home")
def home():
    recipes = mongo.db.recipes.find()
    return render_template("home.html", recipes=recipes)


# Get Recipes
@mst.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Get Categories
@mst.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# One recipe
@mst.route("/recipe/<recipe_id>")
def recipe_display(recipe_id):
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    mongo.db.recipes.update_one(
        {'_id': ObjectId(recipe_id)}, {'$inc': {'views': int(1)}})
    return render_template("/recipe-display.html", recipe=recipe_db)


# Add Category
@mst.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Edit Category
@mst.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        update_category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, update_category)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))
    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete Category
@mst.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# Add Recipec
@mst.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if session.get("user"):
        if request.method == "POST":
            veg_no_veg = "on" if request.form.get("veg_no_veg") else "off"
            add_recipe = {
                "recipe_name": request.form.get("recipe_name").lower(),
                "category_name": request.form.get("category_name").lower(),
                "img_url": request.form.get("img_url"),
                "ingredients": request.form.get("ingredients").lower(),
                "method": request.form.get("method").lower(),
                "tools": request.form.get("tools").lower(),
                "shared_by": session["user"],
                "veg_no_veg": veg_no_veg
            }
            mongo.db.recipes.insert_one(add_recipe)
            flash("Your Recipe Successfully Added")
            return redirect(url_for("get_recipes"))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add_recipe.html", categories=categories)
    else:
        return render_template("login.html")


@mst.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        veg_no_veg = "on" if request.form.get("veg_no_veg") else "off"
        submit_update_recipe = {
            "recipe_name": request.form.get("recipe_name").lower(),
            "category_name": request.form.get("category_name").lower(),
            "img_url": request.form.get("img_url"),
            "ingredients": request.form.get("ingredients").lower(),
            "method": request.form.get("method").lower(),
            "tools": request.form.get("tools").lower(),
            "shared_by": session["user"],
            "veg_no_veg": veg_no_veg
        }
        mongo.db.recipes.update(
            {"_id": ObjectId(recipe_id)}, submit_update_recipe)
        flash("Your Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Delete Recipe
@mst.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe has been Successfully Deleted")
    return redirect(url_for("profile", username=session['user']))


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
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user = session.get("user").lower()
    user_recipes = list(
        mongo.db.recipes.find({"shared_by": session["user"]}))
    if user is not None:
        return render_template(
            "profile.html", username=username, recipes=user_recipes,)
    else:
        return render_template("/login.html")


@mst.route("/logout")
def logout():
    # remove user from session cookies
    flash("You hav been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Search
@mst.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    if len(recipes) == 0:
        flash(f"Sorry, There are no recipe containing  {query} :( ")
    else:
        flash(f"We found {len(recipes)} result(s) :)")
    return render_template("recipes.html", recipes=recipes)


# Errors
@mst.errorhandler(404)
def not_found(e):
    return render_template("/error404.html")


if __name__ == "__main__":
    mst.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
