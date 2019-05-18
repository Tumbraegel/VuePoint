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

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , vuepoint.py

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

@app.route('/')
def show_all_tasks():
    db = get_db()
    cur = db.execute('select title, taskDescription, dueDate from tasks order by id desc')
    tasks = cur.fetchall()
    form = WTPostForm()
    return render_template('show_all_tasks.html', tasks=tasks, form=form)

@app.route('/add', methods=['POST'])
def add_task():
    form = WTPostForm()
    if form.validate ():
        task = {
            'title': form.data['title'],
            'taskDescription': form.data['taskDescription'],
            'dueDate': form.data['dueDate']
            }
    else:
        for  err in form.errors.items():
            flash(str(err))    
    db = get_db()
    db.execute('insert into tasks (title, taskDescription, dueDate, taskState) values (?, ?, ?, 0)',
                 [task['title'], task['taskDescription'], task['dueDate']])
    db.commit()
    flash('New task was successfully posted')
    return redirect(url_for('show_all_tasks'))

class WTPostForm(Form):
    title = StringField('title', validators=[DataRequired()])
    taskDescription = StringField('taskDescription', validators=[DataRequired()])
    dueDate = DateField('dueDate', validators=[DataRequired()])

