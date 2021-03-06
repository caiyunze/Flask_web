#!flask/bin/python
#coding=utf-8
from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

tasks = [
    {  'id': 1, 'title': u'Buy groceries', 'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',  'done': False
    },
    {   'id': 2, 'title': u'Learn Python', 'description': u'Need to find a good Python tutorial on the web', 'done': False
    }
]

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        abort(400,'aaaaaa')
    return jsonify({'tasks': tasks})

@app.errorhandler(400)
def not_found(error):
    print error
    return error



if __name__ == '__main__':
    app.run(debug=True)