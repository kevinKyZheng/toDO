from app import app,db
from flask.ext.script import Manager, Server
from app.models import Todo
manager = Manager(app)
manager.add_command("runserver",
         Server(host='0.0.0.0',port=5000, use_debugger=True))

@manager.command
def save_todo():
    db.create_all()
    todo = Todo(content="123")
    db.session.add(todo)
    db.session.commit()

if __name__ =='__main__':
    manager.run()