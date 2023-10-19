from flask import Flask, request, render_template, url_for, redirect
from static.models import ToDo, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_app()

@app.get('/')
def home():
    todo_list = toDo.query.all()
    return render_template('templates/index.html', todo_list = todo_list, title = 'Home Page')

@app.post('/add')
def add():
    title = request.form.get('title')
    new_todo =  ToDo(title=title, is_complete = False)
    
    db.session.all(new_todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.get('/update/<int:todo_id>')
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    todo.is_coplete = not todo.is_comlete
    db.session.commit()
    return redirect(url_for('home'))

@app.get('/delete/<int:todo_id>')
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))