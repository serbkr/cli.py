import sys
import argparse
import json
import os
from classmodule import MyClass
from funcmodule import load_tasks, save_tasks, task_exists, mark_task_completed                  

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

def main():
    print('In main')
    tasks = load_tasks()
    print(f'Loaded {len(tasks)} tasks.')
    
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for adding a task
    add_parser = subparsers.add_parser('add', help='Add new task')
    add_parser.add_argument('task', type=str, help='The task to add')

    # Subparser for listing tasks
    List_parser = subparsers.add_parser('list', help='List all tasks')

    # Subparser for removing a task
    remove_parser = subparsers.remove_parser('remove', help='Remove a task')
    remove_parser.add_argument('index', type=int, help='The index of the task to remove')

    args = parser.parse_args()

    if args.command == 'add':
        new_task = {'description': args.task, 'completed': False}
        tasks.append(new_task)
        save_tasks(tasks)
        print(f'Task added: "{args.task}"')
    elif args.command == 'list':
        if not tasks:
            print("No tasks found.")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "✓" if task['completed'] else "✗"
                print(f"{index}. [{status}] {task['description']}")
    elif args.command == 'remove':
        if 0 < args.index <= len(tasks):
            removed_task = tasks.pop(args.index - 1)
            save_tasks(tasks)
            print(f'Task removed: "{removed_task["description"]}"')
        else:
            print("Invalid task index.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
