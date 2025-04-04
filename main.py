import flask
from flask import *
from flask import json
from datetime import timedelta
import pymysql
#创建flask程序
app = Flask(__name__,
            static_url_path='/static',#静态文件路径，当程序解析到/static的时候不要用解析路由的方法解析，要用提取文件的方式解析
            static_folder='static',#放静态文件的文件夹,将a.png放到static文件夹中,当你访问127.0.0.1：8888/static/a.png时可以访问到文件本身
            template_folder='templates'#模板文件
           )

@app.route('/login')
def form():
    return render_template('login.html')

@app.route('/judge',methods=['POST'])
def judge():
    if request.method == "POST":
        username = request.form.get("uname")
        password = request.form.get("passwd")
        print("用户名提交了"+username+"密码提交了"+password)
    if username == "独爱zj":
        return flask.redirect(flask.url_for('search'))
    return render_template('wrong.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/output',methods=['POST'])
def output():
    id = request.form.get("id")
    # 打开数据库
    db = pymysql.connect(host="localhost", user="root", password="roottoor", db="haha")
    # 创建游标对象
    cursor = db.cursor()
    # sql语句
    sql = "select * from table1"
    # 执行sql
    cursor.execute(sql)
    # 确认
    db.commit()
    list1 = []
    for i in range(4):
        data = cursor.fetchone()
        # 取出来的是元组，可以转化为列表
        li = list(data)
        list1.append(li)
    id1 = int(id)
    return flask.render_template("output.html",id = id,item = list1[id1-1][1],quality=list1[id1-1][2])
    pass
    #404重定向
@app.errorhandler(404)
def pahe_not_found(e):
    return 'You are Wrong !',404
    pass
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True) #0.0.0.0代表着主机上所有的ip