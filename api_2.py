from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world", 200 # returns 201 error code to the caller
  
@app.route("/name", methods=["GET"])
def getname():
  """
  Returns the name dictionary below to the caller as JSON
  """
  name = {
    "name": "Mackenna",
  }
  return jsonify(name) # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well

@app.route("/hello/<name>", methods=["GET"])
def gethello(<name>):
  """
  Returns the hello_name dictionary below to the caller as JSON
  """
  hello_name = {
    "message": "Hello there" name,
  }
  return jsonify(hello_name) 


@app.route("/sum", methods=["POST"])
def sum():
  r = request.get_json() # parses the POST request body as JSON
  s = r["a"] + r["b"] # adds JSON dict parameter "a" and "b" together
  return s, 200
  
@app.route("/distance", methods=["POST"])
def distance():
  r = request.get_json() # parses the POST request body as JSON
  dist = r["a"]*r["a"] + r["b"]*r["b"] # adds JSON dict parameter "a" and "b" together
  dist_return = {
    "distance": dist,
    "a": r["a"],
    "b": r["b"]
  }
  return jsonify(dist_return), 200
