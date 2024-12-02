#Create a route that accepts a name as part of the URL and displays "Hello, [name]!".
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def greet(name):
    return f"Hello {name}"