import flask
from flask import request

app = flask.Flask(__name__)

task = []

@app.route('/')
def index():
	return 'OK!'

@app.route('/task', methods=['GET'])
def get_task():
	return flask.jsonify(task)

@app.route('/task', methods=['POST'])
def create_task():
        data = request.json
        if 'id' in data and 'name' in data and 'describe' in data and 'run to' in data and 'date of creation' in data:
            name = data['name']
            if len(list(filter(lambda x: x['name'] == name, task))) != 0:
                return flask.jsonify({
                    'code': 2,
                    'message': 'задание уже есть в системе'
                })
            task.append(data)
            return flask.jsonify({
                'code': 0,
                'message': 'Task created'
            })
        return flask.jsonify({
            'code': 1,
            'message': 'У задания есть обязательные поля: name, describe , run to, date of creation '
        })

@app.route('/task/<int:id>', methods=['DELETE'])
def delete_task(id: int):
	global task
	index_for_delete = None
	for idx, user in enumerate(task):
		if user['id'] == id:
			index_for_delete = idx
			break
	if index_for_delete is not None:
		del task[index_for_delete]
		return 'Успешно удалено'
	else:
		return '<p style="color:red;">Task not found</p>'


@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id: int):
    global task
    data = request.json
    if len(task) >= task_id:
        if 'name' in data and 'describe' in data and 'run to' in data and 'date of creation' in data:
            task[task_id - 1] = data
            return flask.jsonify({
                'code': 0,
                'message': 'Task updated!'
            })
        return flask.jsonify({
            'code': 1,
            'message': 'У задания есть обязательные поля: name, describe , run to, date of creation '
        })
    return flask.jsonify({
        'code': 3,
        'message': 'Task not found!'
        })


if __name__ == '__main__':
  app.run('localhost', 6000)