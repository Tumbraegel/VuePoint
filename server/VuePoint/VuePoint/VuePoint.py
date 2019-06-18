# Adapted from http://flask.pocoo.org/docs/0.12/tutorial/ and https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
# to initialize a new db run 'flask initdb' in terminal
# all the imports
import os
import sqlite3
import json
from datetime import datetime
from datetime import date
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import ModelSchema
from  flask_wtf  import  Form
from  wtforms  import  StringField, DateField, IntegerField
from  wtforms.validators  import  DataRequired
from  sqlalchemy  import  create_engine, orm
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
ma = Marshmallow(app)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    taskDescription = Column(String)
    dueDate = Column(Date)
    taskState = Column(Integer)
    flag = Column(String)

Base.metadata.create_all(engine)

class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/list', methods=['GET', 'POST'])
def show_all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        newTask = extractDataFromRequest()
        addTask(newTask)
        response_object['message'] = 'task added!'
    response_object['tasks'] = tasks_schema.dump(session.query(Task))
    return jsonify(response_object)

@app.route("/")
def allTasks():
    result = tasks_schema.dump(session.query(Task))
    return jsonify(result)

def extractDataFromRequest():
    postData = request.get_json()
    title = getOrElse(postData, 'title', 'test title')
    taskDescription = getOrElse(postData, 'taskDescription', 'test description')
    dateFormat = '%Y-%m-%d'
    dueDate = getOrElse(postData, 'dueDate', date.today().strftime(dateFormat))
    flag = getOrElse(postData, 'flag', '')
    newTask= Task(title=title, taskDescription=taskDescription, dueDate=datetime.strptime(dueDate, dateFormat), taskState=0, flag=flag)
    return newTask

def getOrElse(source, attributeName, defaultValue):
    value = source.get(attributeName)
    if value == "":
        value = defaultValue
    return value

def addTask(new_task):
    session.add(new_task)
    session.commit()

def sqlAlchemyTasksToViewTask(tasks):
    viewTasks = []
    for task in tasks:
        viewTasks.append({'id': task.id, 'title': task.title, 'taskDescription': task.taskDescription, 
        'dueDate': task.dueDate, 'taskState': task.taskState, 'flag': task.flag})
    return viewTasks

@app.route('/list/<taskId>', methods=['GET', 'DELETE', 'POST', 'PUT'])
def single_task(taskId):
    response_object = {'status': 'success'}
    if request.method == 'DELETE':
        deleteTask(taskId)
        response_object['message'] = 'Task removed!'
    elif request.method == 'PUT':
        checkTaskStatus(taskId)
        response_object['message'] = 'Task status updated!'
    elif request.method == 'POST':
        updateTask(taskId)
        response_object['message'] = 'Task updated!'
    else:
        response_object['tasks'] = sqlAlchemyTasksToViewTask(session.query(Task).all())
    return jsonify(response_object)

def deleteTask(taskId):
    session.delete(getTaskBy(taskId))
    session.commit()

def updateTask(taskId):
    deleteTask(taskId)
    addTask(taskId)

def getTaskBy(taskId):
    return session.query(Task).filter(Task.id==taskId).first()

def checkTaskStatus(taskId): 
    currentTask = getTaskBy(taskId)
    if currentTask.taskState == 0:
        markTaskAsDone(taskId)
    else:
        markTaskAsNotDone(taskId)

def markTaskAsDone(taskId):
    currentTask = getTaskBy(taskId)
    if currentTask.taskState == 0:
        currentTask.taskState = 1
    session.commit()

def markTaskAsNotDone(taskId):
    currentTask = getTaskBy(taskId)
    if currentTask.taskState == 1:
        currentTask.taskState = 0
    session.commit()

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# class WTPostForm(Form):
#     title = StringField('title', validators=[DataRequired()])
#     taskDescription = StringField('taskDescription', validators=[DataRequired()])
#     dueDate = DateField('dueDate', validators=[DataRequired()])
