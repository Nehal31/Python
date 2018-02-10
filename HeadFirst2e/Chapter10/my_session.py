
from flask import Flask,session

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route('/setuser/<user>')
def setuser(user : str)-> str:
    session['user'] = user
    return 'User set value is :'+session['user']

@app.route('/getuser')
def getuser()->str:
    return 'your set user value is'+session['user']

if __name__ == '__main__':
    app.run(debug=True)
