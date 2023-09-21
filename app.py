from flask import Flask, jsonify

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
  
  return app