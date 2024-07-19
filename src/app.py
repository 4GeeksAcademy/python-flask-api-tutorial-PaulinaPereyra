from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label": "My first task", "done": False}]
new_todo = [{"label": "My first task", "done": True}]

@app.route('/todos', methods=['GET'])
def get_todos():
    json_data = jsonify(todos)
    return json_data

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    deleted_todo = todos.pop(position)
    print("Deleted todo:", deleted_todo)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
