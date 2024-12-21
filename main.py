from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template("index.html", tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))


@app.route('/delete/<int:id>')
def delete_task(id):
    if len(tasks) > id and id > -1 and len(tasks):
        return tasks.pop(id)


@app.route('/edit/<int:id>')
def edit(id):
    if id > -1 and id < len(tasks):
        task = tasks[id]
        return render_template('edit.html', task_id=id, task=task)
    return redirect('/')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if len(tasks) > id and id > -1 and len(tasks):
        tasks[id] = request.form.get('new_task')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
