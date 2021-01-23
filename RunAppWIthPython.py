from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return "Hello"

if __name__ == "__main__":
  app.run(debug=True)
  ##app.run(debug=True) produces an error

## flask run if name of file is app.py
## export FLASK_APP=script.py
## flask run
## **debug mode
## export FLASK_DEBUG=1
## flask run
