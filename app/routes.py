from flask import Blueprint, jsonify
from app.models import Task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({"message": "TaskFlow API is running!"})

@main.route('/api/tasks')
def get_tasks():
    # Заглушка для API
    return jsonify({"tasks": []})
