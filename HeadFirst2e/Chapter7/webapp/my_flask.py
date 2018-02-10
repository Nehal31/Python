"""

"""

from flask import Flask,render_template,request,escape,session
from search import match_value
from DBcm import UseDatabase
from checker import checker_logged_in

app = Flask(__name__)
app.secret_key = 'guessmysecrectkey'

app.config['dbconfig'] = {
    'host' : '127.0.0.1',
    'user' : 'match',
    'password' : 'matchpwd',
    'database' : 'matchlogDB'
    }

def log_request(req: 'flask_rquest', res: str) ->None:
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """ INSERT INTO log (phrase,letters,ip,browser_string,results)
                VALUES(%s,%s,%s,%s,%s)"""

        log = (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res,)

        cursor.execute(_SQL,log)
    

@app.route('/')
def take_value():
    return ''

@app.route('/home')
def home_page() ->'html':
    return render_template('home.html',title='Welcome to match for letters ')

@app.route('/match',methods=['GET','POST'])
def match() ->'html':
    phrase = request.form['phrase']
    letter = request.form['letters']
    result = str(match_value(phrase,letter))
    log_request(request, result)
    title = 'Here are your results:'
    return render_template('result.html',header=title, phrase = phrase ,letters = letter,result = result)

@app.route('/logview')
@checker_logged_in
def log_file_view() -> 'html':
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        
        _SQL = """ Select id,phrase,letters,ip,browser_string,results FROM log"""
        cursor.execute(_SQL)
        content = cursor.fetchall()
    title = 'Here are Logs of Match'
    row_titles =['id','phrase','letters','Remote Address','Browser','Results']
    return render_template('logs.html',header = title,row_title = row_titles, row_items = content)

@app.route('/login')
def login()->str:
    session['logged_in'] = True
    return 'you are logged in '

@app.route('/logout')
def logout()->str:
    if 'logged_in' in session:
        session.pop('logged_in')
    return 'you are logged out '


__name__ = '__main__'
	
app.run(debug=True)
