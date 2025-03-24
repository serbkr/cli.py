import json
import os

tasks_file = 'tasks.json'

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as f:
            return json.load(f)
    return[]

def save_tasks(tasks):
    """Save tasks to the json file"""
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)

def task_exists(task_description, tasks):
    """Check if a task already exists"""
    return any(task['description'] == task_description for task in tasks)

def mark_task_completed(task_index, tasks):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        return True
    return False
