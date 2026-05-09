from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

TASK_FILE = "/tmp/tasks.txt"

def get_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as f:
        return f.readlines()

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.writelines(tasks)

@app.route("/")
def home():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")

    if task:
        tasks = get_tasks()
        tasks.append(task + "\n")
        save_tasks(tasks)

    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    tasks = get_tasks()

    if 0 <= id < len(tasks):
        tasks.pop(id)
        save_tasks(tasks)

    return redirect("/")

application = app

if __name__ == "__main__":
    app.run(debug=True)