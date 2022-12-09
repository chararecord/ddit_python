from flask import Flask, render_template
from flask.globals import request
from flask.json import jsonify
import time
app = Flask(__name__)

@app.route('/')
@app.route('/thread')
def thread():
    return render_template('thread.html')

@app.route('/ajax_thread1', methods=['POST'])
def ajax_thread1():
    time.sleep(1)
    a = '1'
    return jsonify(a=a)

@app.route('/ajax_thread2', methods=['POST'])
def ajax_thread2():
    a = '1'
    return jsonify(a=a)

if __name__ == '__main__':
    app.run(debug=True)