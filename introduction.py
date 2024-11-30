from flask import Flask
app = Flask(__name__)

@app.route('/monologue')
def monologue():
    return """My name is olamide ayeni.
         I am a female.
         and i am 21 years old.
             """


@app.route('/')
def hello():
    return "Hello, welcome to my page"
             
             