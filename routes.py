from flask import Flask, request, render_template, url_for, redirect
from models import ToDo, db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

app = create_app()

@app.get('/')
def home():
    todo_list = ToDo.query.all()
    return render_template('index.html')

@app.post('/add')
def add():
    title = request.form.get('title')
    new_todo = ToDo(title=title, is_complete=False)
    
    db.session.add(new_todo)  # Поправив помилку тут (замість `all` має бути `add`)
    db.session.commit()
    return redirect(url_for('home'))

@app.get('/update/<int:todo_id>')
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()  # Поправив тут (замість `ToDo` має бути `todo`)
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for('home'))

@app.get('/delete/<int:todo_id>')
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()  # Поправив тут (замість `ToDo` має бути `todo`)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))