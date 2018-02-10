from flask import Flask
from vsearch import fun4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello World from flask'

@app.route('/fun4letters')
def do_vowels() -> set:
    return fun4letters('hello how are you')

app.run()
