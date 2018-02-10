"""

"""

from flask import Flask,render_template,request,escape,session,copy_current_request_context
from search import match_value
from DBcm import UseDatabase, ConnectionError, CredentialError, SQLError 
from checker import checker_logged_in
from threading import Thread
from time import sleep


app = Flask(__name__)
app.secret_key = 'guessmysecrectkey'

app.config['dbconfig'] = {
    'host' : '127.0.0.1',
    'user' : 'match',
    'password' : 'matchpwd',
    'database' : 'matchlogDB'
    }
   

@app.route('/')
def take_value():
    return ''

@app.route('/home')
def home_page() ->'html':
    return render_template('home.html',title='Welcome to match for letters ')

@app.route('/match',methods=['GET','POST'])
def match() ->'html':

    @copy_current_request_context
    def log_request(req: 'flask_rquest', res: str) ->None:
        sleep(20)
        with UseDatabase(app.config['dbconfig']) as cursor:
            
            _SQL = """ INSERT INTO log (phrase,letters,ip,browser_string,results)
                    VALUES(%s,%s,%s,%s,%s)"""

            log = (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res,)
            
            cursor.execute(_SQL,log)
        
    phrase = request.form['phrase']
    letter = request.form['letters']
    result = str(match_value(phrase,letter))
    try:
        t = Thread(target = log_request, args =(request,result) )
        t.start()
        
    except Exception as err:
        print('***** Logging failed with error ',str(err))
        
    title = 'Here are your results:'    
    return render_template('result.html',header=title, phrase = phrase ,letters = letter,result = result)

@app.route('/logview')
@checker_logged_in
def log_file_view() -> 'html':
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            
            _SQL = """ Select id,phrase,letters,ip,browser_string,results FROM log"""
            cursor.execute(_SQL)
            content = cursor.fetchall()
        title = 'Here are Logs of Match'
        row_titles =['id','phrase','letters','Remote Address','Browser','Results']
        return render_template('logs.html',header = title,row_title = row_titles, row_items = content)


    except ConnectionError as err:
        print('Is your database switched on ? Error :',err)
    except CredentialError as err:
        print('User-id ? Password issue . Error :',str(err))
    except SQLError as err:
        print('Is your Query Correct ? Error :',str(err))
    except Exception as err:
        print('Something went wrong :', str(err))
    return 'Error'


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
