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
from flask_wtf  import  Form
from wtforms  import  StringField, DateField, IntegerField
from wtforms.validators  import  DataRequired
from sqlalchemy  import  create_engine, orm
from sqlalchemy.orm  import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Date
from flask_cors import CORS

app = Flask(__name__) 
app.config.from_object(__name__) 

engine = create_engine('sqlite:///vuePoint.db', connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()

CORS(app, resources={r'/*': {'origins': '*'}})

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'vuePoint.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('VUEPOINT_SETTINGS', silent=True)

Base  = declarative_base()
Base.metadata.create_all(engine)
ma = Marshmallow(app)

def connect_db():
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
    init_db()
    print('Initialized the database.')

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    taskDescription = Column(String)
    dueDate = Column(Date)
    taskState = Column(Integer)
    flag = Column(String)

class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task

# task_schema = TaskSchema()
@app.route('/list', methods=['GET', 'POST'])
def show_all_tasks():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        addTask()
        response_object['message'] = 'task added!'
    tasks_schema = TaskSchema(many=True)
    response_object['tasks'] = tasks_schema.dump(session.query(Task))
    return jsonify(response_object)

def addTask():
    session.add(extractTaskDataFromRequest())
    session.commit()

def extractTaskDataFromRequest():
    postData = request.get_json()
    title = getOrElse(postData, 'title', 'test title')
    taskDescription = getOrElse(postData, 'taskDescription', 'test description')
    dateFormat = '%Y-%m-%d'
    dueDate = getOrElse(postData, 'dueDate', date.today().strftime(dateFormat))
    flag = getOrElse(postData, 'flag', '')
    return Task(title=title, taskDescription=taskDescription, dueDate=datetime.strptime(dueDate, dateFormat), taskState=0, flag=flag)

def getOrElse(source, attributeName, defaultValue):
    value = source.get(attributeName)
    if value == "":
        value = defaultValue
    return value

@app.route('/list/<taskId>', methods=['DELETE', 'POST', 'PUT'])
def single_task(taskId):
    response_object = {'status': 'success'}
    if request.method == 'DELETE':
        deleteTask(taskId)
        response_object['message'] = 'Task removed!'
    elif request.method == 'PUT':
        updateTaskStatus(taskId)
        response_object['message'] = 'Task status updated!'
    else:
        updateTask(taskId)
        response_object['message'] = 'Task updated!'
    tasks_schema = TaskSchema(many=True)
    response_object['tasks'] = tasks_schema.dump(session.query(Task))
    return jsonify(response_object)

def deleteTask(taskId):
    session.delete(getTaskBy(taskId))
    session.commit()

def getTaskBy(taskId):
    return session.query(Task).filter(Task.id==taskId).first()

def updateTask(taskId):
    deleteTask(taskId)
    addTask()

def updateTaskStatus(taskId): 
    currentTask = getTaskBy(taskId)
    if currentTask.taskState == 0:
        currentTask.taskState = 1
    else:
        currentTask.taskState = 0
    session.commit()

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# class WTPostForm(Form):
#     title = StringField('title', validators=[DataRequired()])
#     taskDescription = StringField('taskDescription', validators=[DataRequired()])
#     dueDate = DateField('dueDate', validators=[DataRequired()])
