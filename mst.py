import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


mst = Flask(__name__)

mst.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
mst.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mst.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(mst)


@mst.route("/")
def hello():
    return "Hello World ...  again!"


if __name__ == "__main__":
    mst.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
