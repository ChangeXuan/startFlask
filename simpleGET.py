from flask import Flask, jsonify,abort  #json和跳转

app = Flask(__name__)

#测试用的静态数据
tasks = [
    {
        'id': 1,
        'title': u'This is one',
        'done': False
    },
    {
        'id': 3,
        'title': u'This is three',
        'done': False
    }
]

@app.route('/')
def init():
    return 'hi GET'

#xxx/test/qinzixuan -> 返回json数据
#xxx/test/qinzixuan -> 返回error
@app.route('/test/<name>', methods=['GET'])
def get_one(name):
    if name == 'qinzixuan':
        return jsonify({'tasks':tasks})
    else:
        return "error"

#按照tasks中的id进行查找，如果id存在，则输出id是test_id的那一项json数据
@app.route('/test/<int:test_id>', methods=['GET'])
def get_two(test_id):
    task = filter(lambda t: t['id'] == test_id,tasks)
    if len(task) == 0:
        #跳转到404界面
        abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def page_not_found(e):
    return '<h1>404 - Not Found</h1>'

if __name__ == '__main__':
    app.run(debug=True)
