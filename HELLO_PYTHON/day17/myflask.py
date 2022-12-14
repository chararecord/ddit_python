from flask import Flask, render_template
from flask.globals import request
from flask.json import jsonify
app = Flask(__name__)

@app.route('/')
@app.route('/main')
def teacher():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)