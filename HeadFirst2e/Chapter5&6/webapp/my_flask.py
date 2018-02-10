"""
This is a simple web application using Flask

"""

from flask import Flask,render_template,request,escape
from search import match_value

app = Flask(__name__)

def log_request(req: 'flask_rquest', res: str) ->None:
    with open('match.log','a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file = log, sep='|')

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
    return render_template('result.html',header=title,phrase = phrase ,letters = letter,result = result)

@app.route('/logview')
def log_file_view() -> 'html':
    try:
        with open('match.log','r')as file:
            logs = []
            for line in file:
                logs.append([])
                for item in line.split('|'):
                    logs[-1].append(escape(item))

        title = 'Here are Logs of Match'
        row_titles =['Form Data','Remote Address','User Agents','Results']
        return render_template('logs.html',header = title,row_title = row_titles, row_items = logs)
    except IOError as ioarr:
        print('File Error',ioarr)

__name__ = '__main__'
	
app.run(debug=True)
