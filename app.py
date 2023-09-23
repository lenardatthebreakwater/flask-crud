from flask import Flask, jsonify, request

languages = [{"name": "Python"}, {"name": "Javascript"}, {"name": "C"}]

def create_app():
  app = Flask(__name__)
  
  @app.route("/lang", methods=["GET"])
  def getAll():
    return jsonify({"languages": languages})

  @app.route("/lang/<string:name>")
  def getOne(name):
    language = []
    
    for lang in languages:
      if lang["name"] == name:
        language.append(lang)
    
    return jsonify({"language": language[0]})
  
  @app.route("/lang", methods=["POST"]) 
  def addOne():
    languages.append({"name": request.json["name"]})
    
    return jsonify({"languages": languages})
    
  @app.route("/lang/<string:name>", methods=["PUT"])
  def updateOne(name):
    language = []
    
    for lang in languages:
      if lang["name"] == name:
        language.append(lang)
    
    language[0]["name"] = request.json["name"]
    
    return jsonify({"language": language[0]})

  return app