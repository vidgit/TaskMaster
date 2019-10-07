from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
DB = SQLAlchemy(APP)

class Todo(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    content = DB.Column(DB.String(200), nullable=False)
    date_created = DB.Column(DB.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@APP.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        try:
            DB.session.add(new_task)
            DB.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'+e

    else:
        task = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=task)
    

if __name__ == "__main__":
    APP.run(debug=True)
