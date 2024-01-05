from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

@app.get("/")
def home():
    todos = Todo.query.all()
    return render_template("home.html", todos=todos)

@app.post("/add")
def add():
    content = request.form["content"]
    new_todo = Todo(content=content)
    db.session.add(new_todo)
    db.session.commit()
    return redirect("/")

@app.get("/update/<int:todo_id>")
def update_get(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    return render_template("update.html", todo=todo)

@app.post("/update/<int:todo_id>")
def update_post(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.content = request.form["todo_update"]
    db.session.commit()
    return redirect("/")

@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

