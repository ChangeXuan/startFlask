# -*- coding:utf-8 -*-
from flask import Flask, jsonify,abort,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def init():
    return 'hi POST'

@app.route('/post/one', methods=['POST'])
def post_one():
    #判断请求的数据是否为空
    if not request.form:
        abort(400)
    #获取POST表中的各项数据
    return request.form['id']+request.form['title'], 201

@app.route('/post/two', methods=['POST'])
def post_two():
    #判断请求的数据是否为空
    if not request.form:
        abort(400)
    #组建新的json数据
    task = {
        'id': request.form['id'],
        'title': request.form['title'],
        'done': False
    }
    #添加
    tasks.append(task)
    return jsonify({'task': tasks}), 201

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404 - Not Found</h1>'

if __name__ == '__main__':
    app.run(debug=True)
