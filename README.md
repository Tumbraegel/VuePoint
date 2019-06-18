# VuePoint
Student Group Project using Python, Flask and Vue.js

For Windows: 

1. Client-side Vue app in one terminal:

    ```sh
    $ cd client
    $ npm install
    $ npm run dev
    ```

> http://localhost:8080

2. Server-side Flask app in another terminal:

    Install server env
    ```sh
    $ cd server
    $ conda create --name envName
    $ conda activate envName
    (env)$ conda install --file requirements.yml
    ```
    Run the server
    For windows, run the commands seperately and use set instead of export
    ```sh
    cd VuePoint
    pip install --editable . && export FLASK_APP=VuePoint && export FLASK_DEBUG=true && flask run
    ```

    Initialize Database
    ```sh
    flask initdb
    ```

> http://localhost:5000