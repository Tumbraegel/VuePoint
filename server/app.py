from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
# Note: In order to make cross-origin requests - e.g., requests that originate
# from a different protocol, IP address, domain name, or port - you need to
# enable Cross Origin Resource Sharing (CORS)
CORS(app)

TASKS = [
    [{
        'title': 'Office Party',
        'description': 'Buy Cookies',
        'importance':'high'
    }],
    [{
        'title': 'Meeting',
        'description': 'with Jacob from HR',
        'importance':'high'
    },
    {
        'title': 'Coffee Date',
        'description': '@Starbucks',
        'importance':'low'
    }]
]

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/tasks', methods=['GET'])
def all_tasks():
    return jsonify({
        'status': 'success',
        'tasks': TASKS
    })


if __name__ == '__main__':
    app.run()
