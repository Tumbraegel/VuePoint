This application is build using the flask tutorial
http://flask.pocoo.org/docs/0.12/tutorial/dbcon/#tutorial-dbcon

for testing the post route to add books:
curl -X POST http://localhost:5000/list -d \
  '{"title": "1Q84", "taskDescription": "Haruki Murakami"}' \
  -H 'Content-Type: application/json'

or:
  curl -X POST http://localhost:5000/add -d \
  '{"title": "Get healthy", "taskDescription": "I should probably sleep"}' \
  -H 'Content-Type: application/json'