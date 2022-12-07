from flask import Flask, render_template
from day11.dao_mem import DaoMember
from flask.globals import request
app = Flask(__name__)

@app.route('/')
@app.route('/mem_list')
def mem_list():
    dm = DaoMember()
    list = dm.selects()
    return render_template('mem_list.html', list=list)

@app.route('/mem_detail')
def mem_detail():
    dm = DaoMember()
    m_id = request.args.get('m_id')
    mem = dm.select(m_id)
    return render_template('mem_detail.html', mem=mem)

@app.route('/mem_edit')
def mem_edit():
    dm = DaoMember()
    m_id = request.args.get('m_id')
    mem = dm.select(m_id)
    return render_template('mem_edit.html', mem=mem)

@app.route('/mem_edit_act', methods=['post'])
def mem_edit_act():
    dm = DaoMember()
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    cnt = dm.insert(m_id, m_nm, tel, ymd)
    return render_template('mem_edit_act.html', cnt=cnt)

@app.route('/mem_add')
def mem_add():
    return render_template('mem_add.html')

@app.route('/mem_add_act', methods=['post'])
def mem_add_act():
    dm = DaoMember()
    m_id = request.form['m_id']
    m_nm = request.form['m_nm']
    tel = request.form['tel']
    ymd = request.form['ymd']
    cnt = dm.insert(m_id, m_nm, tel, ymd)
    return render_template('mem_add_act.html', cnt=cnt)

@app.route('/mem_del_act', methods=['post'])
def mem_del_act():
    dm = DaoMember()
    m_id = request.form['m_id']
    cnt = dm.delete(m_id)
    return render_template('mem_del_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)