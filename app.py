
## **How to create a virtual Environment with flask **
## py -m venv env ## Created a virtual environment
## env\Scripts\activate ## activated my virtual environment
## pip install flask ## installed flask on my virtual environment
## set FLASK_APP=app **lets flask know what file to look for
## ctr+c to quite app to resart etc 
## deactivate to quite virtual environment

#************ PIPENV ********************
## An alternative to venv
## pip install pipenv
## pipenv install flask
## pipenv shell ## create a name based off current folder

## ** to install packages **
## after virtual enviornemt is activated pipenv package


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
  return "<h1>Hello!</h1>"

@app.route("/query")
def query():
  name = request.args.get('name') or 'Name'
  location = request.args.get('location') or 'Location'
  return "<h1>Hi {}, you are from {}</h1>".format(name, location)

@app.route('/<name>')
def call(name):
  return "<h1>Hello! {}!</h1>".format(name)

@app.route('/home', methods=["POST", "GET"], defaults={'name': 'user'})
@app.route("/home/<name>", methods=['POST','GET'])
def home(name):
  return "<h1>Hello {}, you are on the home page!</h1>".format(name)

@app.route("/json")
def json():
  return jsonify({"Name": "Michael", "age":"40", "job":"Programmer"})

@app.route("/theform")
def theform():
  return '''<form method="POST" action="/process">
          <input type="text" name="name">
          <input type="text" name="location">
          <input type="submit" value="Submit">
          </form>
          '''
@app.route('/process', methods=["POST"])
def process():
  name= request.form["name"]
  location = request.form["location"]

  return "<h1>Hello {}. You are from {}.  You have submittted the form successfully!.</h1>".format(name, location)



if __name__ == "__main__":
  app.run(debug=True)
 