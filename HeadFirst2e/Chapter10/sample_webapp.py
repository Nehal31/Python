
from flask import Flask,session
from checker import checker_logged_in

app = Flask(__name__)
app.secret_key = 'guessmysecretkey'

@app.route('/')
def page()->str:
    return 'Tish is first page'

@app.route('/page1')
@checker_logged_in
def page1()->str:
    return 'you are in page 1'

@app.route('/page2')
@checker_logged_in
def page2()->str:
    return 'you are in page 2'
    

@app.route('/page3')
@checker_logged_in
def page3()->str:
    return 'you are in page 3'

@app.route('/login')
def login()->str:
    session['logged_in'] = True
    return 'you are logged in '

@app.route('/logout')
def logout()->str:
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'you are logged out '


if __name__ == '__main__':
    app.run(debug=True)


