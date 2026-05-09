from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

TASK_FILE = "tasks.txt"

@app.route("/")
def home():
    if not os.path.exists(TASK_FILE):
        open(TASK_FILE, "w").close()

    with open(TASK_FILE, "r") as f:
        tasks = f.readlines()

    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")

    if task:
        with open(TASK_FILE, "a") as f:
            f.write(task + "\n")

    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    with open(TASK_FILE, "r") as f:
        tasks = f.readlines()

    if 0 <= id < len(tasks):
        tasks.pop(id)

    with open(TASK_FILE, "w") as f:
        f.writelines(tasks)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)