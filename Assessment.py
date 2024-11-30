# A program that reads a file and outputs the content of the file on a web page.
from flask import Flask
app = Flask(__name__)

def read_file(file):
    with open(file, "r") as f:
        return f.read()
    

@app.route('/')
def home():
    file = "document.txt"
    content = read_file(file)
    return content
    