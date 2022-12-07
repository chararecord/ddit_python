from flask import Flask, render_template
from flask.globals import request
from day10.dao_emp import DaoEmp
app = Flask(__name__)

@app.route('/')
@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    list = de.selects()
    return render_template('emp_list.html', list=list)

@app.route('/emp_detail')
def emp_detail():
    de = DaoEmp()
    e_id = request.args.get('e_id')
    emp = de.select(e_id)
    return render_template('emp_detail.html', emp=emp)

@app.route('/emp_edit')
def emp_edit():
    de = DaoEmp()
    e_id = request.args.get('e_id')
    emp = de.select(e_id)
    return render_template('emp_edit.html', emp=emp)

@app.route('/emp_edit_act', methods=['post'])
def emp_edit_act():
    de = DaoEmp()
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    cnt = de.update(e_id, e_name, sex, addr)
    return render_template('emp_edit_act.html', cnt=cnt)

@app.route('/emp_add')
def emp_add():
    de = DaoEmp()
    return render_template('emp_add.html')

@app.route('/emp_add_act', methods=['post'])
def emp_add_act():
    de = DaoEmp()
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    sex = request.form['sex']
    addr = request.form['addr']
    cnt = de.insert(e_id, e_name, sex, addr)
    return render_template('emp_add_act.html', cnt=cnt)

@app.route('/emp_del_act', methods=['post'])
def emp_del_act():
    de = DaoEmp()
    e_id = request.form['e_id']
    cnt = de.delete(e_id)
    return render_template('emp_del_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)