# Adapted from http://flask.pocoo.org/docs/0.12/tutorial/
# to initialize a new db run 'flask initdb' in terminal
# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from  flask_wtf  import  Form
from  wtforms  import  StringField
from wtforms import DateField
from  wtforms.validators  import  DataRequired
from  sqlalchemy  import  create_engine
from  sqlalchemy.orm  import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Date

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , vuepoint.py

engine = create_engine('sqlite:///vuePoint.db')
Session = sessionmaker(bind=engine)
session = Session()

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

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    taskDescription = Column(String)
    dueDate = Column(Date)
    taskState = Column(Integer)

Base.metadata.create_all(engine)

@app.route('/')
def show_all_tasks():
    tasks = session.query(Task).all()
    form = WTPostForm()
    return render_template('show_all_tasks.html', tasks=tasks, form=form)

@app.route('/add', methods=['POST'])
def add_task():
    form = WTPostForm()
    if form.validate ():
        new_task = Task(title=form.data['title'], taskDescription=form.data['taskDescription'], dueDate=form.data['dueDate'], taskState=0)
        session.add(new_task)
        session.commit()
    else:
        for  err in form.errors.items():
            flash(str(err))
    flash('New task was successfully posted')
    return redirect(url_for('show_all_tasks'))

class WTPostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    taskDescription = StringField('taskDescription', validators=[DataRequired()])
    dueDate = DateField('dueDate', validators=[DataRequired()])

