# Adapted from http://flask.pocoo.org/docs/0.12/tutorial/ and https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
# to initialize a new db run 'flask initdb' in terminal
# all the imports
import os
import sqlite3
import json
import datetime
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from  flask_wtf  import  Form
from  wtforms  import  StringField, DateField, IntegerField
from  wtforms.validators  import  DataRequired
from  sqlalchemy  import  create_engine
from  sqlalchemy.orm  import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Date, JSON
from flask_cors import CORS

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , vuepoint.py

engine = create_engine('sqlite:///vuePoint.db', connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()

# enable CORS //https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
CORS(app, resources={r'/*': {'origins': '*'}})

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'vuePoint.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('VUEPOINT_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

Base  = declarative_base()

mock_tasks =[
{
    'id': '1',
    'title': 'Office Party',
    'dueDate': 'Friday',
    'taskDescription': 'Buy Cookies',
    # importance: 'high',
    'taskState': '1',
    },
    {
    'id': '2',
    'title': 'Ticket #25',
    'dueDate': 'Tuesday',
    'taskDescription': 'Needs to be done ASAP',
    # importance: 'high',
    'taskState': '0',
    },
    {
    'id': '3',
    'title': 'Grocery Shopping',
    'dueDate': 'Weekend',
    'taskDescription': '@fancy supermarket',
    # importance: 'low',
    'taskState': '0',
    },
    {
    'id': '4',
    'title': 'Sprint 34 Deadline',
    'dueDate': 'Wednesday',
    'taskDescription': 'To-Do: Tickets #73, #75, #79',
    # importance: 'high',
    'taskState': '0',
    },
    {
    'id': '5',
    'title': 'Sprint Review',
    'dueDate': 'Wednesday',
    'taskDescription': 'Having an existential crisis',
    # important: 'high',
    'taskState': '0',
    }
]

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    taskDescription = Column(String)
    dueDate = Column(Date)
    taskState = Column(Integer)
    flag = Column(String)

Base.metadata.create_all(engine)

@app.route('/list', methods=['GET', 'POST'])
def show_all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        addTask()
        response_object['message'] = 'task added!'
    else:
        # response_object['tasks'] = mock_tasks
        response_object['tasks'] = sqlAlchemyTasksToViewTask(session.query(Task).all())
    return jsonify(response_object)

@app.route('/list/<task_id>', methods=['GET', 'DELETE'])
def single_task(task_id):
    response_object = {'status': 'success'}
    if request.method == 'DELETE':
        deleteTask(task_id)
        response_object['message'] = 'Task removed!'
    else:
        response_object['tasks'] = sqlAlchemyTasksToViewTask(session.query(Task).all())
    return jsonify(response_object)

def addTask():
    post_data = request.get_json()
    new_task = Task(title=post_data.get('title'), taskDescription=post_data.get('taskDescription'),
     dueDate=datetime.date.today(), taskState=0, flag=post_data.get('flag'))
    session.add(new_task)
    session.commit()

def deleteTask(task_id):
    task_to_delete = session.query(Task).filter(Task.id==task_id).first()
    session.delete(task_to_delete)
    session.commit()

def sqlAlchemyTasksToViewTask(tasks):
    viewTasks = []
    for task in tasks:
        viewTasks.append({'id': task.id, 'title': task.title, 'taskDescription': task.taskDescription, 
        'dueDate': task.dueDate, 'taskState': task.taskState, 'flag': task.flag})
    return viewTasks

@app.route('/add', methods=['POST'])
def add_task():
    response_object = {'status': 'success'}
    addTask()
    response_object['message'] = 'task added!'
    return jsonify(response_object)

# @app.route('/delete/<task_id>', methods=['DELETE'])
# def delete_task(task_id):
#    response_object = {'status': 'success'}
#    deleteTask(task_id)
#    response_object['message'] = 'task deleted!'
#    return jsonify(response_object)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# class WTPostForm(Form):
#     title = StringField('title', validators=[DataRequired()])
#     taskDescription = StringField('taskDescription', validators=[DataRequired()])
#     dueDate = DateField('dueDate', validators=[DataRequired()])
