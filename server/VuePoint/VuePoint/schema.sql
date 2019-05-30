-- Adapted from http://flask.pocoo.org/docs/0.12/tutorial/
drop table if EXISTS tasks;
create TABLE tasks(
  id INTEGER PRIMARY KEY autoincrement,
  title text not null,
  taskDescription text,
  dueDate date not null DEFAULT CURRENT_DATE,
  taskState INTEGER not null,
  flag text
);