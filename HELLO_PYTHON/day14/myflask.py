from flask import Flask, render_template
from flask.globals import request
from flask.json import jsonify
from day14.dao_teacher import DaoTeacher
app = Flask(__name__)

@app.route('/')
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/ajax_teacher_list', methods=['POST'])
def ajax_teacher_list():
    # dict = request.get_json()
    dt = DaoTeacher()
    list = dt.selects()
    return jsonify(list=list)

@app.route('/ajax_teacher_one', methods=['POST'])
def ajax_teacher_one():
    dt = DaoTeacher()
    dict = request.get_json()
    t_id = dict['t_id']
    tch = dt.select(t_id)
    return jsonify(tch=tch)

@app.route('/ajax_teacher_add', methods=['POST'])
def ajax_teacher_add():
    dt = DaoTeacher()
    dict = request.get_json()
    t_name = dict['t_name']
    mobile = dict['mobile']
    addr = dict['addr']
    cnt = dt.insert(t_name, mobile, addr)
    return jsonify(cnt=cnt)

@app.route('/ajax_teacher_edit', methods=['POST'])
def ajax_teacher_edit():
    dt = DaoTeacher()
    dict = request.get_json()
    t_id = dict['t_id']
    t_name = dict['t_name']
    mobile = dict['mobile']
    addr = dict['addr']
    cnt = dt.update(t_id, t_name, mobile, addr)
    return jsonify(cnt=cnt)

@app.route('/ajax_teacher_del', methods=['POST'])
def ajax_teacher_del():
    dt = DaoTeacher()
    dict = request.get_json()
    t_id = dict['t_id']
    cnt = dt.delete(t_id)
    return jsonify(cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)