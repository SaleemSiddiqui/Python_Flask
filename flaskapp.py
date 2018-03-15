
from flask import Flask,\
render_template, url_for, \
redirect, request, session, redirect, jsonify
from flask_pymongo import PyMongo
import numpy as np
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 's_database'
app.config['MONGO_URI'] = "mongodb://admin:admin@ds119988.mlab.com:19988/s_database"

mongo = PyMongo(app)

@app.route("/", methods=['GET','POST'])
@app.route("/")
def index():
    check=False
    if request.method == 'POST':
        dataInsert = mongo.db.user
        dataInsert.insert({'user': request.form['user'], 'pass': request.form['pass']})
        check=True
    return render_template("AddData.html", ok=check)

@app.route("/add", methods=['GET','POST'])
def add():
    check=False
    if request.method == 'POST':
        dataInsert = mongo.db.user
        dataInsert.insert({'user': request.form['user'], 'pass': request.form['pass']})
        check=True
    return render_template("AddData.html", ok=check)

@app.route("/search", methods=['GET','POST'])
def search():
    check=False    
    if request.method=='POST':
        checkUser=mongo.db.user
        watchMan=checkUser.find({'user': request.form['user'] , 'pass': request.form['pass']})
        for i in watchMan:
            if i['user']==request.form['user'] and i['pass']==request.form['pass'] :
                check=True
                return render_template("search.html", AO_sDocument="found")
                break

    return render_template("search.html", ok=check)

@app.route("/delete", methods=['GET','POST'])
def delete():
    check=False    
    if request.method=='POST':
        checkUser=mongo.db.user
        watchMan=checkUser.find({'user': request.form['user'] , 'pass': request.form['pass']})
        for i in watchMan:
            if i['user']==request.form['user'] and i['pass']==request.form['pass'] :
                mongo.db.user.remove({"user":i['user']})
                return render_template("search.html", AO_sDocument="deleted")
                break

    return render_template("delete.html", ok=check)

@app.route("/shd")
def api():
    dbAllData=mongo.db.user.find()
    allUsers=[]
    for us in dbAllData:
        allUsers.append({'user': us['user']})

    return jsonify({"Users": allUsers})
app.run(debug=True)