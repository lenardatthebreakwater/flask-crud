from flask import Flask, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
  
db = SQLAlchemy(app)
  
class Language(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  
@app.route("/lang", methods=["GET"])
def getAll():
  languages = []
  
  for language in Language.query.all():
    languages.append({"id": language.id, "name": language.name})
  
  return jsonify({"languages": languages})

@app.route("/lang/<int:id>")
def getOne(id):
  language = Language.query.filter_by(id=id).first()
  
  return jsonify({"language": {"id": language.id, "name": language.name}})

@app.route("/lang", methods=["POST"]) 
def addOne():
  new_language = Language(name=request.json["name"])
  
  db.session.add(new_language)
  db.session.commit()
  
  languages = []
  for language in Language.query.all():
    languages.append({"id": language.id, "name": language.name})
    
  return jsonify({"languages": languages})
    
@app.route("/lang/<int:id>", methods=["PUT"])
def updateOne(id):
  language = Language.query.filter_by(id=id).first()
  
  language.name = request.json["name"]
  db.session.commit()
  
  languages = []
  for language in Language.query.all():
    languages.append({"id": language.id, "name": language.name})
  
  return jsonify({"languages": languages})
  
@app.route("/lang/<int:id>", methods=["DELETE"])
def deleteOne(id):
  language = Language.query.filter_by(id=id).first()
  
  db.session.delete(language)
  db.session.commit()
  
  languages = []
  for lang in Language.query.all():
    languages.append({"id": lang.id, "name": lang.name})
    
  return jsonify({"languages": languages})
  