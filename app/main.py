from flask import Flask
import os
import json
import psycopg2

app = Flask(__name__)

env = os.getenv('APP_ENV')
with open('config/db.{0}.json'.format(env)) as db_conf:
    data = json.load(db_conf)

conn = psycopg2.connect(host=data['host'], user=data['user'])

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
