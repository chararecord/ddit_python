from flask import Flask, render_template
from flask.globals import request
from day09.dao_sample import DaoSample
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/param')
def param():
    a = request.args.get('a', 'babo')
    return 'param:'+a

@app.route('/post', methods=['get','post'])
def post():
    a = request.form['a']
    return 'post:'+a

@app.route('/sample')
def sample():
    ds = DaoSample()
    list = ds.selects()
    return str(list)

@app.route('/view')
def view():
    a = "밍갱징"
    b = ["쿠키","빵","점심","저녁"]
    c = [
            {'col01':'1','col02':'1','col03':'1'},
            {'col01':'2','col02':'2','col03':'2'},
            {'col01':'3','col02':'3','col03':'3'}
        ]
    ds = DaoSample()
    d = ds.selects()
    return render_template('view.html', a=a,b=b,c=c,d=d)

if __name__ == '__main__':
    app.run(debug=True)