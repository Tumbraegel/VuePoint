This application is build using the flask tutorial
http://flask.pocoo.org/docs/0.12/tutorial/dbcon/#tutorial-dbcon

for testing the post route to add books:
curl -X POST http://localhost:5000/list -d \
  '{"title": "Doctors Appointment", "taskDescription": "prepare mentally", "flag": "work"}' \
  -H 'Content-Type: application/json'
